from __future__ import annotations
import os

from queue import Queue
from exo import proc, DRAM

ROOT_DIR = "/workspaces/project/"
CHIPYARD_DIR = f"{ROOT_DIR}/chipyard/"
GEMMINI_TEST_DIR = f"{CHIPYARD_DIR}/generators/gemmini/software/gemmini-rocc-tests/"

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

BASE_C = """// See LICENSE for license details.

#include <stdint.h>
#include <stddef.h>
#include <assert.h>
#include <stdlib.h>
#include <stdio.h>
#ifndef BAREMETAL
#include <sys/mman.h>
#endif
#include "include/gemmini_testutils.h"

void generated_operation(const elem_t* In, const elem_t* Weights, elem_t* Out);

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

  generated_operation((elem_t *) In, (elem_t *) Identity, (elem_t *) Out);

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

def do_exocc()
    raise NotImplementedError(f"TODO: move over the evaluate_generated.generated_exo function to python for speed")

def do_compile() -> None:
    os.sys(
        f"cd {GEMMINI_TEST_DIR} && "
        "./build.sh -s &> /dev/null"
    )

def do_sim() -> str:
    read_output = os.popen(
        "spike --extension=gemmini "
        "-l --log=$PROJ_ROOT/log "
        f"{GEMMINI_TEST_DIR}/build/bareMetalC/generated_harness-baremetal"
    )

    return read_output

def get_score(stdout_lines: list[str], trace_file: str = f"{ROOT_DIR}/log") -> tuple[bool, float]:
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
                out_file: str = f"{GEMMINI_TEST_DIR}/bareMetalC/generated_harness.c",
    ) -> float:
    total_c = BASE_C + transpiled_c

    with open(out_file, "w") as f:
        f.write(total_c)

    do_compile()
    _, score = get_score(
        stdout=do_sim()
    )

    return score

def 

class PersistentQueue:

    def __init__(self, *args, persistence_file: str = f"persistent_queue.pkl", **kwargs)
        queue = Queue(*args, **kwargs)
        self.out_file = persistence_file
        with open(self.out_file, "wb") as f:
            pickle.dump(queue, self.out_file)

    def put(self, item):
        with open(self.out_file, "r+b") as f:
            queue = pickle.load(f)
            queue.put(item)

            f.seek(0, 0) # move write cursor to beginning of file
            pickle.dump(queue, f)

    def get(self):
        with open(self.out_file, "r+b") as f:
            queue = pickle.load(f)
            ret_val = queue.get()

            f.seek(0, 0) # move write cursor to beginning of file
            pickle.dump(queue, f)
        
        return ret_val
