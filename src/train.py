from __future__ import annotations
import os

from exo import proc, DRAM

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

def evaluate_out(total_string: str) -> tuple[bool, int]:
    """Returns tuple (correct_code?, num_of_instructions) """

    with open("out.py", "w") as f:
        f.write(total_string)

    success_table = {"PASS\n":True, "FAIL\n":False}

    out = os.popen("/workspaces/project/evaluate_generated.sh 2>&1").readlines()[0]

    if out not in success_table:
        return False, -1
        raise ValueError(f"Unexpected output: {out}")

    is_success = success_table[out]

    if not is_success:
        return is_success, -1
    
    with open("/workspaces/project/log", 'r') as f:
        num_lines = len(f.readlines())

    return is_success, num_lines


