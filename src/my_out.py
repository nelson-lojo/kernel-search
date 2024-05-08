from __future__ import annotations
from exo import proc, DRAM
from exo.platforms.rvv import *
@proc
def generated_operation(In: i8[16, 16] @ DRAM, Weights: i8[16, 16] @ DRAM,
                        Out: i8[16, 16] @ DRAM):
    for j in seq(0, 16):
        for i in seq(0, 16):
            OutStaged: i8[16, 16] @ DRAM
            for i0 in seq(0, 16):
                for i1_out in seq(0, 16 / 12):
                    for i1_in in seq(0, 12):
                        OutStaged[i0, 12 * i1_out +
                                  i1_in] = Out[i0, 12 * i1_out + i1_in]
                for i1_in in seq(0, 16 % 12):
                    OutStaged[i0,
                              i1_in + 16 / 12 * 12] = Out[i0,
                                                          i1_in + 16 / 12 * 12]
            for k in seq(0, 16):
                OutStaged[i, j] += In[i, k] * Weights[k, j]
            for i0 in seq(0, 16):
                for i1 in seq(0, 16):
                    Out[i0, i1] = OutStaged[i0, i1]