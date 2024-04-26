from __future__ import annotations
from exo import proc, DRAM
from exo.stdlib.scheduling import *
from exo.platforms.gemmini import *

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
gemmini = rename(generated_operation, "generated_operation_scheduled")
gemmini = reorder_loops(gemmini, "j k")
gemmini = reorder_loops(gemmini, "i k")

## then fuse the two inner loops
gemmini = fuse_loops(gemmini, "k j")

## split the outer loop to reduce memory traffic
gemmini = split(gemmini, 4, ["i_outer", "i_inner"])

## inline the window expression to reduce memory allocation
gemmini = inline_window(gemmini, "In[i_outer*4 + i_inner, k]")
gemmini = inline_window(gemmini, "Weights[k, j]")

## stage the memory access to reduce memory traffic
gemmini = stage_mem(gemmini, "Out[i_outer*4 + i_inner, j]", "Out_staged", 0, 16)

## bind the expression to a new buffer to reduce memory allocation
gemmini = bind_expr(gemmini, "In[i_outer*4 + i_inner, k] * Weights[k, j]", "temp_buffer")

## reorder the statements to reduce dependencies
gemmini = reorder_stmts(gemmini, "temp_buffer =...", "Out_staged[i_outer*4 + i_inner, j] +=...")

## simplify the code to reduce overhead
gemmini = simplify(gemmini)

## set the precision and memory type for the buffers
gemmini = set_precision(gemmini, "temp_buffer", "i8")
gemmini = set_memory(gemmini, "temp_buffer", "SRAM")

print(gemmini.get_ast())  # print the scheduled AST