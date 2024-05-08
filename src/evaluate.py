from __future__ import annotations
import os
 
# from exo import proc, DRAM
import pickle
import concurrent.futures

from time import sleep

ROOT_DIR = "/workspaces/project/"
CHIPYARD_DIR = f"{ROOT_DIR}/chipyard/"
GEMMINI_TEST_DIR = f"{CHIPYARD_DIR}/generators/gemmini/software/gemmini-rocc-tests/"
SPIKE_LOG_FILE = f"{ROOT_DIR}/log"

ARTIFACT_DIR = f"{ROOT_DIR}/artifacts/"
os.makedirs(ARTIFACT_DIR, exist_ok=True)

QUEUE_FILE = f"{ARTIFACT_DIR}/evaluation_queue.pkl"

BASE_EXO = """from __future__ import annotations
from exo import proc, DRAM
from exo.stdlib.scheduling import *

# Algorithm definition
@proc
def generated_operation(
    In: i8[16, 16] @ DRAM,
    Weights: i8[16, 16] @ DRAM,
    Out: i8[16, 16] @ DRAM,
):
    for i in seq(0, 16):
        for j in seq(0, 16):
            for k in seq(0, 16):
                Out[i, j] += In[i, k] * Weights[k, j]

# Now we create a schedule to improve performance!
## first switch to "output stationary"
# gemmini = rename(generated_operation, "generated_operation_scheduled")
# gemmini = reorder_loops(gemmini, "j k")
# gemmini = reorder_loops(gemmini, "i k")

## then """

BASE_C = r"""// See LICENSE for license details.

#include <stdint.h>
#include <stddef.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#ifndef BAREMETAL
#include <sys/mman.h>
#endif
#include "include/gemmini_testutils.h"

void generated_operation(void *ctxt, const int8_t* In, const int8_t* Weights, int8_t* Out);

int main() {
#ifndef BAREMETAL
    if (mlockall(MCL_CURRENT | MCL_FUTURE) != 0) {
      perror("mlockall failed");
      exit(1);
    }
#endif

  // printf("Flush Gemmini TLB of stale virtual addresses\n");
  gemmini_flush(0);

  // printf("Initialize our input and output matrices in main memory\n");
  elem_t In[DIM][DIM];
  elem_t Out[DIM][DIM];

  elem_t Identity[DIM][DIM];
  for (size_t i = 0; i < DIM; i++)
    for (size_t j = 0; j < DIM; j++)
      Identity[i][j] = i == j;

  generated_operation(0x0, (elem_t *) In, (elem_t *) Identity, (elem_t *) Out);

  // printf("Check whether \"In\" and \"Out\" matrices are identical\n");
  if (!is_equal(In, Out)) {
    /*
    printf("Input and output matrices are different!\n");
    printf("\"In\" matrix:\n");
    printMatrix(In);
    printf("\"Out\" matrix:\n");
    printMatrix(Out);
    printf("\n");
    */
    printf("FAIL\n");
    exit(0);
  }

  printf("PASS\n");
  exit(0);
}


"""

def do_exocc():
    raise NotImplementedError(f"TODO: move over the evaluate_generated.generated_exo function to python for speed")

def write_c_code(generated_c: str, out_file: str):
    total_c = BASE_C + generated_c

    with open(out_file, "w") as f:
        f.write(total_c)

def do_compile() -> None:
    os.popen(
        f"cd {GEMMINI_TEST_DIR} && "
        "./build.sh -s &> /dev/null"
    ).read()

def do_sim() -> list[str]:
    read_output = os.popen(
        "spike --extension=gemmini "
        f"-l --log={SPIKE_LOG_FILE} "
        f"{GEMMINI_TEST_DIR}/build/bareMetalC/generated_harness-baremetal"
    ).readlines()

    return read_output

def get_score(stdout_lines: list[str], trace_file: str = SPIKE_LOG_FILE) -> tuple[bool, int]:
    success_table = {"PASS\n":True, "FAIL\n":False}

    out = stdout_lines[0]
    if out not in success_table:
        return False, -1
        raise ValueError(f"Unexpected output: {out}")

    is_success = success_table[out]

    if not is_success:
        return is_success, -1
    
    with open(trace_file, 'r') as f:
        num_lines = len(f.readlines())

    return is_success, num_lines


def evaluate_out(total_exo_string: str) -> tuple[bool, int]:
    """Returns tuple (correct_code?, num_of_instructions) """

    with open("out.py", "w") as f:
        f.write(total_exo_string)

    do_exocc()
    do_compile()
    out = do_sim()

    return get_score(out)


def evaluate_c( transpiled_c: str, 
                precomputed_scores: PersistentMap,
                out_file: str = f"{GEMMINI_TEST_DIR}/bareMetalC/generated_harness.c",
    ) -> int:

    old_score = precomputed_scores.get(transpiled_c, None)
    if old_score is not None:
        return old_score

    write_c_code(transpiled_c, out_file)

    do_compile()
    _, score = get_score(
        stdout_lines=do_sim()
    )

    precomputed_scores.put(
        transpiled_c, score
    )

    return score


class PersistentDataStruct:

    def __init__(self, default_value, filename: str, overwrite: bool = False):
        self.out_file = filename
        if overwrite or not os.path.isfile(self.out_file):
            with open(self.out_file, "wb") as f:
                pickle.dump(default_value, f)

    def get_raw(self):
        with open(self.out_file, "rb") as f:
            return pickle.load(f)

    def _get(self, *args, **kwargs):
        raise NotImplementedError()

    def get(self, *args, **kwargs):
        while True:
            try:
                ret_val = self._get(*args, **kwargs)
                break
            except IOError:
                sleep(0.1)
                continue

        return ret_val

    def _put(self, *args, **kwargs):
        raise NotImplementedError()

    def put(self, *args, **kwargs):
        while True:
            try:
                ret_val = self._put(*args, **kwargs)
                break
            except IOError:
                sleep(0.1)
                continue

        return ret_val

class PersistentQueue(PersistentDataStruct):

    def __init__(self, persistence_file: str = f"{ARTIFACT_DIR}/persistent_queue.pkl", overwrite: bool = False):
        super().__init__([ ], persistence_file, overwrite) # default would be Queue(*args, **kwargs) if it could be pickled

    def _put(self, *items, **_):
        with open(self.out_file, "r+b") as f:
            queue = pickle.load(f)

            queue.extend(items)

            f.seek(0, 0) # move write cursor to beginning of file
            pickle.dump(queue, f)

    def _get(self, *_, **__):
        with open(self.out_file, "r+b") as f:
            queue = pickle.load(f)

            ret_val = queue.pop(0) if len(queue) > 0 else None

            f.seek(0, 0) # move write cursor to beginning of file
            pickle.dump(queue, f)
        
        return ret_val

class PersistentMap(PersistentDataStruct):

    def __init__(self, filename: str = f"{ARTIFACT_DIR}/persistent_map.pkl", overwrite: bool = False):
        super().__init__({ }, filename, overwrite)

    def _put(self, key, value): # pyright: ignore[reportIncompatibleMethodOverride]
        with open(self.out_file, "r+b") as f:
            mapping = pickle.load(f)

            mapping.update({ key : value })

            f.seek(0, 0) # move write cursor to beginning of file
            pickle.dump(mapping, f)

    def _get(self, key, default = None): # pyright: ignore[reportIncompatibleMethodOverride]
        with open(self.out_file, "r+b") as f:
            mapping = pickle.load(f)

            return mapping.get(key, default)

if __name__ == "__main__":
    eval_queue = PersistentQueue(
        persistence_file=QUEUE_FILE,
        overwrite=False
    )

    computed_evaluations = PersistentMap(
        filename=f"{ARTIFACT_DIR}/evaluations.pkl",
        overwrite=False
    )

    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            future = None

            while True:
                c_code = eval_queue.get() # load the code chunk
                if c_code is None:
                    print(f"No more items in queue! Sleeping for 1 second")
                    sleep(1)
                    continue

                if future is not None: # join a previous thread if it was running to avoid file conflicts
                    score = future.result()
                    future = executor.submit(evaluate_c, c_code, computed_evaluations) # spawn new job

                else:
                    future = executor.submit(evaluate_c, c_code, computed_evaluations) # spawn new job

    except KeyboardInterrupt as _:
        print(f"> Caught Keyboard Interrupt: Exiting.")
