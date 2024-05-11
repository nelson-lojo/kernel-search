from __future__ import annotations
from exo import proc, DRAM
from exo.platforms.rvv import *
@proc
def generated_operation(In: i8[16, 16] @ DRAM, Weights: i8[16, 16] @ DRAM,
                        Out: i8[16, 16] @ DRAM):
    for i in seq(0, 16):
        for j in seq(0, 16):
            OutStaged: i8[16, 16] @ DRAM
            OutStagedStaged: i8[64, 4] @ DRAM
            OutStagedStaged[0, 0] = Out[0, 0]
            OutStagedStaged[0, 1] = Out[0, 1]
            OutStagedStaged[0, 2] = Out[0, 2]
            OutStagedStaged[0, 3] = Out[0, 3]
            OutStagedStaged[1, 0] = Out[0, 4]
            OutStagedStaged[1, 1] = Out[0, 5]
            OutStagedStaged[1, 2] = Out[0, 6]
            OutStagedStaged[1, 3] = Out[0, 7]
            OutStagedStaged[2, 0] = Out[0, 8]
            OutStagedStaged[2, 1] = Out[0, 9]
            OutStagedStaged[2, 2] = Out[0, 10]
            OutStagedStaged[2, 3] = Out[0, 11]
            OutStagedStaged[3, 0] = Out[0, 12]
            OutStagedStaged[3, 1] = Out[0, 13]
            OutStagedStaged[3, 2] = Out[0, 14]
            OutStagedStaged[3, 3] = Out[0, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged[4 * i0_1 + i1 / 4,
                                                          i1 % 4]
            OutStagedStaged_1: i8[64, 4] @ DRAM
            OutStagedStaged_1[4, 0] = Out[1, 0]
            OutStagedStaged_1[4, 1] = Out[1, 1]
            OutStagedStaged_1[4, 2] = Out[1, 2]
            OutStagedStaged_1[4, 3] = Out[1, 3]
            OutStagedStaged_1[5, 0] = Out[1, 4]
            OutStagedStaged_1[5, 1] = Out[1, 5]
            OutStagedStaged_1[5, 2] = Out[1, 6]
            OutStagedStaged_1[5, 3] = Out[1, 7]
            OutStagedStaged_1[6, 0] = Out[1, 8]
            OutStagedStaged_1[6, 1] = Out[1, 9]
            OutStagedStaged_1[6, 2] = Out[1, 10]
            OutStagedStaged_1[6, 3] = Out[1, 11]
            OutStagedStaged_1[7, 0] = Out[1, 12]
            OutStagedStaged_1[7, 1] = Out[1, 13]
            OutStagedStaged_1[7, 2] = Out[1, 14]
            OutStagedStaged_1[7, 3] = Out[1, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_1[4 * i0_1 + i1 / 4,
                                                            i1 % 4]
            OutStagedStaged_2: i8[64, 4] @ DRAM
            OutStagedStaged_2[8, 0] = Out[2, 0]
            OutStagedStaged_2[8, 1] = Out[2, 1]
            OutStagedStaged_2[8, 2] = Out[2, 2]
            OutStagedStaged_2[8, 3] = Out[2, 3]
            OutStagedStaged_2[9, 0] = Out[2, 4]
            OutStagedStaged_2[9, 1] = Out[2, 5]
            OutStagedStaged_2[9, 2] = Out[2, 6]
            OutStagedStaged_2[9, 3] = Out[2, 7]
            OutStagedStaged_2[10, 0] = Out[2, 8]
            OutStagedStaged_2[10, 1] = Out[2, 9]
            OutStagedStaged_2[10, 2] = Out[2, 10]
            OutStagedStaged_2[10, 3] = Out[2, 11]
            OutStagedStaged_2[11, 0] = Out[2, 12]
            OutStagedStaged_2[11, 1] = Out[2, 13]
            OutStagedStaged_2[11, 2] = Out[2, 14]
            OutStagedStaged_2[11, 3] = Out[2, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_2[4 * i0_1 + i1 / 4,
                                                            i1 % 4]
            OutStagedStaged_3: i8[64, 4] @ DRAM
            OutStagedStaged_3[12, 0] = Out[3, 0]
            OutStagedStaged_3[12, 1] = Out[3, 1]
            OutStagedStaged_3[12, 2] = Out[3, 2]
            OutStagedStaged_3[12, 3] = Out[3, 3]
            OutStagedStaged_3[13, 0] = Out[3, 4]
            OutStagedStaged_3[13, 1] = Out[3, 5]
            OutStagedStaged_3[13, 2] = Out[3, 6]
            OutStagedStaged_3[13, 3] = Out[3, 7]
            OutStagedStaged_3[14, 0] = Out[3, 8]
            OutStagedStaged_3[14, 1] = Out[3, 9]
            OutStagedStaged_3[14, 2] = Out[3, 10]
            OutStagedStaged_3[14, 3] = Out[3, 11]
            OutStagedStaged_3[15, 0] = Out[3, 12]
            OutStagedStaged_3[15, 1] = Out[3, 13]
            OutStagedStaged_3[15, 2] = Out[3, 14]
            OutStagedStaged_3[15, 3] = Out[3, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_3[4 * i0_1 + i1 / 4,
                                                            i1 % 4]
            OutStagedStaged_4: i8[64, 4] @ DRAM
            OutStagedStaged_4[16, 0] = Out[4, 0]
            OutStagedStaged_4[16, 1] = Out[4, 1]
            OutStagedStaged_4[16, 2] = Out[4, 2]
            OutStagedStaged_4[16, 3] = Out[4, 3]
            OutStagedStaged_4[17, 0] = Out[4, 4]
            OutStagedStaged_4[17, 1] = Out[4, 5]
            OutStagedStaged_4[17, 2] = Out[4, 6]
            OutStagedStaged_4[17, 3] = Out[4, 7]
            OutStagedStaged_4[18, 0] = Out[4, 8]
            OutStagedStaged_4[18, 1] = Out[4, 9]
            OutStagedStaged_4[18, 2] = Out[4, 10]
            OutStagedStaged_4[18, 3] = Out[4, 11]
            OutStagedStaged_4[19, 0] = Out[4, 12]
            OutStagedStaged_4[19, 1] = Out[4, 13]
            OutStagedStaged_4[19, 2] = Out[4, 14]
            OutStagedStaged_4[19, 3] = Out[4, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_4[4 * i0_1 + i1 / 4,
                                                            i1 % 4]
            OutStagedStaged_5: i8[64, 4] @ DRAM
            OutStagedStaged_5[20, 0] = Out[5, 0]
            OutStagedStaged_5[20, 1] = Out[5, 1]
            OutStagedStaged_5[20, 2] = Out[5, 2]
            OutStagedStaged_5[20, 3] = Out[5, 3]
            OutStagedStaged_5[21, 0] = Out[5, 4]
            OutStagedStaged_5[21, 1] = Out[5, 5]
            OutStagedStaged_5[21, 2] = Out[5, 6]
            OutStagedStaged_5[21, 3] = Out[5, 7]
            OutStagedStaged_5[22, 0] = Out[5, 8]
            OutStagedStaged_5[22, 1] = Out[5, 9]
            OutStagedStaged_5[22, 2] = Out[5, 10]
            OutStagedStaged_5[22, 3] = Out[5, 11]
            OutStagedStaged_5[23, 0] = Out[5, 12]
            OutStagedStaged_5[23, 1] = Out[5, 13]
            OutStagedStaged_5[23, 2] = Out[5, 14]
            OutStagedStaged_5[23, 3] = Out[5, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_5[4 * i0_1 + i1 / 4,
                                                            i1 % 4]
            OutStagedStaged_6: i8[64, 4] @ DRAM
            OutStagedStaged_6[24, 0] = Out[6, 0]
            OutStagedStaged_6[24, 1] = Out[6, 1]
            OutStagedStaged_6[24, 2] = Out[6, 2]
            OutStagedStaged_6[24, 3] = Out[6, 3]
            OutStagedStaged_6[25, 0] = Out[6, 4]
            OutStagedStaged_6[25, 1] = Out[6, 5]
            OutStagedStaged_6[25, 2] = Out[6, 6]
            OutStagedStaged_6[25, 3] = Out[6, 7]
            OutStagedStaged_6[26, 0] = Out[6, 8]
            OutStagedStaged_6[26, 1] = Out[6, 9]
            OutStagedStaged_6[26, 2] = Out[6, 10]
            OutStagedStaged_6[26, 3] = Out[6, 11]
            OutStagedStaged_6[27, 0] = Out[6, 12]
            OutStagedStaged_6[27, 1] = Out[6, 13]
            OutStagedStaged_6[27, 2] = Out[6, 14]
            OutStagedStaged_6[27, 3] = Out[6, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_6[4 * i0_1 + i1 / 4,
                                                            i1 % 4]
            OutStagedStaged_7: i8[64, 4] @ DRAM
            OutStagedStaged_7[28, 0] = Out[7, 0]
            OutStagedStaged_7[28, 1] = Out[7, 1]
            OutStagedStaged_7[28, 2] = Out[7, 2]
            OutStagedStaged_7[28, 3] = Out[7, 3]
            OutStagedStaged_7[29, 0] = Out[7, 4]
            OutStagedStaged_7[29, 1] = Out[7, 5]
            OutStagedStaged_7[29, 2] = Out[7, 6]
            OutStagedStaged_7[29, 3] = Out[7, 7]
            OutStagedStaged_7[30, 0] = Out[7, 8]
            OutStagedStaged_7[30, 1] = Out[7, 9]
            OutStagedStaged_7[30, 2] = Out[7, 10]
            OutStagedStaged_7[30, 3] = Out[7, 11]
            OutStagedStaged_7[31, 0] = Out[7, 12]
            OutStagedStaged_7[31, 1] = Out[7, 13]
            OutStagedStaged_7[31, 2] = Out[7, 14]
            OutStagedStaged_7[31, 3] = Out[7, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_7[4 * i0_1 + i1 / 4,
                                                            i1 % 4]
            OutStagedStaged_8: i8[64, 4] @ DRAM
            OutStagedStaged_8[32, 0] = Out[8, 0]
            OutStagedStaged_8[32, 1] = Out[8, 1]
            OutStagedStaged_8[32, 2] = Out[8, 2]
            OutStagedStaged_8[32, 3] = Out[8, 3]
            OutStagedStaged_8[33, 0] = Out[8, 4]
            OutStagedStaged_8[33, 1] = Out[8, 5]
            OutStagedStaged_8[33, 2] = Out[8, 6]
            OutStagedStaged_8[33, 3] = Out[8, 7]
            OutStagedStaged_8[34, 0] = Out[8, 8]
            OutStagedStaged_8[34, 1] = Out[8, 9]
            OutStagedStaged_8[34, 2] = Out[8, 10]
            OutStagedStaged_8[34, 3] = Out[8, 11]
            OutStagedStaged_8[35, 0] = Out[8, 12]
            OutStagedStaged_8[35, 1] = Out[8, 13]
            OutStagedStaged_8[35, 2] = Out[8, 14]
            OutStagedStaged_8[35, 3] = Out[8, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_8[4 * i0_1 + i1 / 4,
                                                            i1 % 4]
            OutStagedStaged_9: i8[64, 4] @ DRAM
            OutStagedStaged_9[36, 0] = Out[9, 0]
            OutStagedStaged_9[36, 1] = Out[9, 1]
            OutStagedStaged_9[36, 2] = Out[9, 2]
            OutStagedStaged_9[36, 3] = Out[9, 3]
            OutStagedStaged_9[37, 0] = Out[9, 4]
            OutStagedStaged_9[37, 1] = Out[9, 5]
            OutStagedStaged_9[37, 2] = Out[9, 6]
            OutStagedStaged_9[37, 3] = Out[9, 7]
            OutStagedStaged_9[38, 0] = Out[9, 8]
            OutStagedStaged_9[38, 1] = Out[9, 9]
            OutStagedStaged_9[38, 2] = Out[9, 10]
            OutStagedStaged_9[38, 3] = Out[9, 11]
            OutStagedStaged_9[39, 0] = Out[9, 12]
            OutStagedStaged_9[39, 1] = Out[9, 13]
            OutStagedStaged_9[39, 2] = Out[9, 14]
            OutStagedStaged_9[39, 3] = Out[9, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_9[4 * i0_1 + i1 / 4,
                                                            i1 % 4]
            OutStagedStaged_10: i8[64, 4] @ DRAM
            OutStagedStaged_10[40, 0] = Out[10, 0]
            OutStagedStaged_10[40, 1] = Out[10, 1]
            OutStagedStaged_10[40, 2] = Out[10, 2]
            OutStagedStaged_10[40, 3] = Out[10, 3]
            OutStagedStaged_10[41, 0] = Out[10, 4]
            OutStagedStaged_10[41, 1] = Out[10, 5]
            OutStagedStaged_10[41, 2] = Out[10, 6]
            OutStagedStaged_10[41, 3] = Out[10, 7]
            OutStagedStaged_10[42, 0] = Out[10, 8]
            OutStagedStaged_10[42, 1] = Out[10, 9]
            OutStagedStaged_10[42, 2] = Out[10, 10]
            OutStagedStaged_10[42, 3] = Out[10, 11]
            OutStagedStaged_10[43, 0] = Out[10, 12]
            OutStagedStaged_10[43, 1] = Out[10, 13]
            OutStagedStaged_10[43, 2] = Out[10, 14]
            OutStagedStaged_10[43, 3] = Out[10, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_10[4 * i0_1 + i1 / 4,
                                                             i1 % 4]
            OutStagedStaged_11: i8[64, 4] @ DRAM
            OutStagedStaged_11[44, 0] = Out[11, 0]
            OutStagedStaged_11[44, 1] = Out[11, 1]
            OutStagedStaged_11[44, 2] = Out[11, 2]
            OutStagedStaged_11[44, 3] = Out[11, 3]
            OutStagedStaged_11[45, 0] = Out[11, 4]
            OutStagedStaged_11[45, 1] = Out[11, 5]
            OutStagedStaged_11[45, 2] = Out[11, 6]
            OutStagedStaged_11[45, 3] = Out[11, 7]
            OutStagedStaged_11[46, 0] = Out[11, 8]
            OutStagedStaged_11[46, 1] = Out[11, 9]
            OutStagedStaged_11[46, 2] = Out[11, 10]
            OutStagedStaged_11[46, 3] = Out[11, 11]
            OutStagedStaged_11[47, 0] = Out[11, 12]
            OutStagedStaged_11[47, 1] = Out[11, 13]
            OutStagedStaged_11[47, 2] = Out[11, 14]
            OutStagedStaged_11[47, 3] = Out[11, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_11[4 * i0_1 + i1 / 4,
                                                             i1 % 4]
            OutStagedStaged_12: i8[64, 4] @ DRAM
            OutStagedStaged_12[48, 0] = Out[12, 0]
            OutStagedStaged_12[48, 1] = Out[12, 1]
            OutStagedStaged_12[48, 2] = Out[12, 2]
            OutStagedStaged_12[48, 3] = Out[12, 3]
            OutStagedStaged_12[49, 0] = Out[12, 4]
            OutStagedStaged_12[49, 1] = Out[12, 5]
            OutStagedStaged_12[49, 2] = Out[12, 6]
            OutStagedStaged_12[49, 3] = Out[12, 7]
            OutStagedStaged_12[50, 0] = Out[12, 8]
            OutStagedStaged_12[50, 1] = Out[12, 9]
            OutStagedStaged_12[50, 2] = Out[12, 10]
            OutStagedStaged_12[50, 3] = Out[12, 11]
            OutStagedStaged_12[51, 0] = Out[12, 12]
            OutStagedStaged_12[51, 1] = Out[12, 13]
            OutStagedStaged_12[51, 2] = Out[12, 14]
            OutStagedStaged_12[51, 3] = Out[12, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_12[4 * i0_1 + i1 / 4,
                                                             i1 % 4]
            OutStagedStaged_13: i8[64, 4] @ DRAM
            OutStagedStaged_13[52, 0] = Out[13, 0]
            OutStagedStaged_13[52, 1] = Out[13, 1]
            OutStagedStaged_13[52, 2] = Out[13, 2]
            OutStagedStaged_13[52, 3] = Out[13, 3]
            OutStagedStaged_13[53, 0] = Out[13, 4]
            OutStagedStaged_13[53, 1] = Out[13, 5]
            OutStagedStaged_13[53, 2] = Out[13, 6]
            OutStagedStaged_13[53, 3] = Out[13, 7]
            OutStagedStaged_13[54, 0] = Out[13, 8]
            OutStagedStaged_13[54, 1] = Out[13, 9]
            OutStagedStaged_13[54, 2] = Out[13, 10]
            OutStagedStaged_13[54, 3] = Out[13, 11]
            OutStagedStaged_13[55, 0] = Out[13, 12]
            OutStagedStaged_13[55, 1] = Out[13, 13]
            OutStagedStaged_13[55, 2] = Out[13, 14]
            OutStagedStaged_13[55, 3] = Out[13, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_13[4 * i0_1 + i1 / 4,
                                                             i1 % 4]
            OutStagedStaged_14: i8[64, 4] @ DRAM
            OutStagedStaged_14[56, 0] = Out[14, 0]
            OutStagedStaged_14[56, 1] = Out[14, 1]
            OutStagedStaged_14[56, 2] = Out[14, 2]
            OutStagedStaged_14[56, 3] = Out[14, 3]
            OutStagedStaged_14[57, 0] = Out[14, 4]
            OutStagedStaged_14[57, 1] = Out[14, 5]
            OutStagedStaged_14[57, 2] = Out[14, 6]
            OutStagedStaged_14[57, 3] = Out[14, 7]
            OutStagedStaged_14[58, 0] = Out[14, 8]
            OutStagedStaged_14[58, 1] = Out[14, 9]
            OutStagedStaged_14[58, 2] = Out[14, 10]
            OutStagedStaged_14[58, 3] = Out[14, 11]
            OutStagedStaged_14[59, 0] = Out[14, 12]
            OutStagedStaged_14[59, 1] = Out[14, 13]
            OutStagedStaged_14[59, 2] = Out[14, 14]
            OutStagedStaged_14[59, 3] = Out[14, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1, i1] = OutStagedStaged_14[4 * i0_1 + i1 / 4,
                                                             i1 % 4]
            OutStagedStaged_15: i8[1 * 64, 4] @ DRAM
            OutStagedStaged_15[1 * 60 + 0 / 4, 0 % 4] = Out[15, 0]
            OutStagedStaged_15[1 * 60 + 1 / 4, 1 % 4] = Out[15, 1]
            OutStagedStaged_15[1 * 60 + 2 / 4, 2 % 4] = Out[15, 2]
            OutStagedStaged_15[1 * 60 + 3 / 4, 3 % 4] = Out[15, 3]
            OutStagedStaged_15[1 * 61 + 0 / 4, 0 % 4] = Out[15, 4]
            OutStagedStaged_15[1 * 61 + 1 / 4, 1 % 4] = Out[15, 5]
            OutStagedStaged_15[1 * 61 + 2 / 4, 2 % 4] = Out[15, 6]
            OutStagedStaged_15[1 * 61 + 3 / 4, 3 % 4] = Out[15, 7]
            OutStagedStaged_15[1 * 62 + 0 / 4, 0 % 4] = Out[15, 8]
            OutStagedStaged_15[1 * 62 + 1 / 4, 1 % 4] = Out[15, 9]
            OutStagedStaged_15[1 * 62 + 2 / 4, 2 % 4] = Out[15, 10]
            OutStagedStaged_15[1 * 62 + 3 / 4, 3 % 4] = Out[15, 11]
            OutStagedStaged_15[1 * 63 + 0 / 4, 0 % 4] = Out[15, 12]
            OutStagedStaged_15[1 * 63 + 1 / 4, 1 % 4] = Out[15, 13]
            OutStagedStaged_15[1 * 63 + 2 / 4, 2 % 4] = Out[15, 14]
            OutStagedStaged_15[1 * 63 + 3 / 4, 3 % 4] = Out[15, 15]
            for i0_1 in seq(0, 16):
                for i1 in seq(0, 16):
                    OutStaged[i0_1,
                              i1] = OutStagedStaged_15[1 *
                                                       (4 * i0_1 + i1 / 4) +
                                                       i1 % 4 / 4, i1 % 4 % 4]
            for k in seq(0, 16):
                OutStaged[i, j] += In[i, k] * Weights[k, j]
            for i1 in seq(0, 16):
                for i0_out in seq(0, 1):
                    for i0_in_out in seq(0, 1):
                        for i0_in_in in seq(0, 8):
                            Out[i0_in_in + 8 * i0_in_out + 12 * i0_out,
                                i1] = OutStaged[i0_in_in + 8 * i0_in_out +
                                                12 * i0_out, i1]
                    for i0_in_in in seq(0, 4):
                        Out[8 + i0_in_in + 12 * i0_out,
                            i1] = OutStaged[8 + i0_in_in + 12 * i0_out, i1]
                for i0_in_in_out in seq(0, 1 / 4):
                    for i0_in_in_out_1 in seq(0, 4 / 4):
                        for i0_in_in_out_2 in seq(0, 4 / 4):
                            for i0_in_in_out_3 in seq(0, 4 / 4):
                                for i0_in_in_out_4 in seq(0, 4 / 4):
                                    for i0_in_in_out_5 in seq(0, 4 / 4):
                                        for i0_in_in_out_6 in seq(0, 4 / 4):
                                            Out[12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 0))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 0 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           0))))))), i1]
                                            Out[12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 0))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 1 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           0))))))), i1]
                                            Out[12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 0))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 2 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           0))))))), i1]
                                            Out[12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 0))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 3 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           0))))))), i1]
                                            Out[12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 1))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 0 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           1))))))), i1]
                                            Out[12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 1))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 1 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           1))))))), i1]
                                            Out[12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 1))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 2 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           1))))))), i1]
                                            Out[12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 1))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 3 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           1))))))), i1]
                                            Out[12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 2))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 0 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           2))))))), i1]
                                            Out[12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 2))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 1 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           2))))))), i1]
                                            Out[12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 2))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 2 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           2))))))), i1]
                                            Out[12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 2))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 3 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           2))))))), i1]
                                            Out[12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 3))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 0 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           3))))))), i1]
                                            Out[12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 3))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 1 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           3))))))), i1]
                                            Out[12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 3))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 2 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           3))))))), i1]
                                            Out[12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 3))
                                                     ))))),
                                                i1] = OutStaged[
                                                    12 + 3 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           3))))))), i1]
                                        for i0_in_in_out_6 in seq(
                                                0, 4 % 4 / 4):
                                            Out[12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 0 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 0 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          0 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 0 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 1 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          0 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 0 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 2 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          0 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 0 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 3 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          0 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 1 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 0 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          1 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 1 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 1 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          1 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 1 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 2 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          1 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 1 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 3 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          1 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 2 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 0 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          2 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 2 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 1 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          2 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 2 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 2 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          2 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 2 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 3 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          2 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 3 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 0 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          3 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 3 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 1 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          3 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 3 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 2 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          3 + 4 / 4 * 4))))))),
                                                                i1]
                                            Out[12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (4 * i0_in_in_out_6 + 3 +
                                                       4 / 4 * 4))))))),
                                                i1] = OutStaged[12 + 3 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          3 + 4 / 4 * 4))))))),
                                                                i1]
                                        for i0_in_in_out_6 in seq(
                                                0, 4 % 4 % 4 / 4):
                                            for i0_in_in_out_7 in seq(
                                                    0, 4 / 4):
                                                for i0_in_in_in in seq(0, 4):
                                                    Out[12 + 0 + 4 * (
                                                        4 * i0_in_in_out +
                                                        (4 * i0_in_in_out_1 +
                                                         (4 * i0_in_in_out_2 +
                                                          (4 * i0_in_in_out_3 +
                                                           (4 * i0_in_in_out_4 +
                                                            (4 * i0_in_in_out_5 +
                                                             (4 *
                                                              i0_in_in_out_6 +
                                                              (4 *
                                                               i0_in_in_out_7 +
                                                               i0_in_in_in) +
                                                              4 % 4 / 4 * 4 +
                                                              4 / 4 * 4))))))
                                                    ), i1] = OutStaged[
                                                        12 + 0 + 4 *
                                                        (4 * i0_in_in_out +
                                                         (4 * i0_in_in_out_1 +
                                                          (4 * i0_in_in_out_2 +
                                                           (4 * i0_in_in_out_3 +
                                                            (4 *
                                                             i0_in_in_out_4 +
                                                             (4 *
                                                              i0_in_in_out_5 +
                                                              (4 *
                                                               i0_in_in_out_6 +
                                                               (4 *
                                                                i0_in_in_out_7 +
                                                                i0_in_in_in) +
                                                               4 % 4 / 4 * 4 +
                                                               4 / 4 * 4))))))
                                                         ), i1]
                                                    Out[12 + 1 + 4 * (
                                                        4 * i0_in_in_out +
                                                        (4 * i0_in_in_out_1 +
                                                         (4 * i0_in_in_out_2 +
                                                          (4 * i0_in_in_out_3 +
                                                           (4 * i0_in_in_out_4 +
                                                            (4 * i0_in_in_out_5 +
                                                             (4 *
                                                              i0_in_in_out_6 +
                                                              (4 *
                                                               i0_in_in_out_7 +
                                                               i0_in_in_in) +
                                                              4 % 4 / 4 * 4 +
                                                              4 / 4 * 4))))))
                                                    ), i1] = OutStaged[
                                                        12 + 1 + 4 *
                                                        (4 * i0_in_in_out +
                                                         (4 * i0_in_in_out_1 +
                                                          (4 * i0_in_in_out_2 +
                                                           (4 * i0_in_in_out_3 +
                                                            (4 *
                                                             i0_in_in_out_4 +
                                                             (4 *
                                                              i0_in_in_out_5 +
                                                              (4 *
                                                               i0_in_in_out_6 +
                                                               (4 *
                                                                i0_in_in_out_7 +
                                                                i0_in_in_in) +
                                                               4 % 4 / 4 * 4 +
                                                               4 / 4 * 4))))))
                                                         ), i1]
                                                    Out[12 + 2 + 4 * (
                                                        4 * i0_in_in_out +
                                                        (4 * i0_in_in_out_1 +
                                                         (4 * i0_in_in_out_2 +
                                                          (4 * i0_in_in_out_3 +
                                                           (4 * i0_in_in_out_4 +
                                                            (4 * i0_in_in_out_5 +
                                                             (4 *
                                                              i0_in_in_out_6 +
                                                              (4 *
                                                               i0_in_in_out_7 +
                                                               i0_in_in_in) +
                                                              4 % 4 / 4 * 4 +
                                                              4 / 4 * 4))))))
                                                    ), i1] = OutStaged[
                                                        12 + 2 + 4 *
                                                        (4 * i0_in_in_out +
                                                         (4 * i0_in_in_out_1 +
                                                          (4 * i0_in_in_out_2 +
                                                           (4 * i0_in_in_out_3 +
                                                            (4 *
                                                             i0_in_in_out_4 +
                                                             (4 *
                                                              i0_in_in_out_5 +
                                                              (4 *
                                                               i0_in_in_out_6 +
                                                               (4 *
                                                                i0_in_in_out_7 +
                                                                i0_in_in_in) +
                                                               4 % 4 / 4 * 4 +
                                                               4 / 4 * 4))))))
                                                         ), i1]
                                                    Out[12 + 3 + 4 * (
                                                        4 * i0_in_in_out +
                                                        (4 * i0_in_in_out_1 +
                                                         (4 * i0_in_in_out_2 +
                                                          (4 * i0_in_in_out_3 +
                                                           (4 * i0_in_in_out_4 +
                                                            (4 * i0_in_in_out_5 +
                                                             (4 *
                                                              i0_in_in_out_6 +
                                                              (4 *
                                                               i0_in_in_out_7 +
                                                               i0_in_in_in) +
                                                              4 % 4 / 4 * 4 +
                                                              4 / 4 * 4))))))
                                                    ), i1] = OutStaged[
                                                        12 + 3 + 4 *
                                                        (4 * i0_in_in_out +
                                                         (4 * i0_in_in_out_1 +
                                                          (4 * i0_in_in_out_2 +
                                                           (4 * i0_in_in_out_3 +
                                                            (4 *
                                                             i0_in_in_out_4 +
                                                             (4 *
                                                              i0_in_in_out_5 +
                                                              (4 *
                                                               i0_in_in_out_6 +
                                                               (4 *
                                                                i0_in_in_out_7 +
                                                                i0_in_in_in) +
                                                               4 % 4 / 4 * 4 +
                                                               4 / 4 * 4))))))
                                                         ), i1]
                                            for i0_in_in_in in seq(0, 4 % 4):
                                                Out[12 + 0 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          (i0_in_in_in + 4 /
                                                           4 * 4) + 4 % 4 / 4 *
                                                          4 + 4 / 4 * 4))))))
                                                ), i1] = OutStaged[
                                                    12 + 0 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           (i0_in_in_in + 4 /
                                                            4 * 4) + 4 % 4 /
                                                           4 * 4 + 4 / 4 * 4)))
                                                        )))), i1]
                                                Out[12 + 1 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          (i0_in_in_in + 4 /
                                                           4 * 4) + 4 % 4 / 4 *
                                                          4 + 4 / 4 * 4))))))
                                                ), i1] = OutStaged[
                                                    12 + 1 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           (i0_in_in_in + 4 /
                                                            4 * 4) + 4 % 4 /
                                                           4 * 4 + 4 / 4 * 4)))
                                                        )))), i1]
                                                Out[12 + 2 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          (i0_in_in_in + 4 /
                                                           4 * 4) + 4 % 4 / 4 *
                                                          4 + 4 / 4 * 4))))))
                                                ), i1] = OutStaged[
                                                    12 + 2 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           (i0_in_in_in + 4 /
                                                            4 * 4) + 4 % 4 /
                                                           4 * 4 + 4 / 4 * 4)))
                                                        )))), i1]
                                                Out[12 + 3 + 4 * (
                                                    4 * i0_in_in_out +
                                                    (4 * i0_in_in_out_1 +
                                                     (4 * i0_in_in_out_2 +
                                                      (4 * i0_in_in_out_3 +
                                                       (4 * i0_in_in_out_4 +
                                                        (4 * i0_in_in_out_5 +
                                                         (4 * i0_in_in_out_6 +
                                                          (i0_in_in_in + 4 /
                                                           4 * 4) + 4 % 4 / 4 *
                                                          4 + 4 / 4 * 4))))))
                                                ), i1] = OutStaged[
                                                    12 + 3 + 4 *
                                                    (4 * i0_in_in_out +
                                                     (4 * i0_in_in_out_1 +
                                                      (4 * i0_in_in_out_2 +
                                                       (4 * i0_in_in_out_3 +
                                                        (4 * i0_in_in_out_4 +
                                                         (4 * i0_in_in_out_5 +
                                                          (4 * i0_in_in_out_6 +
                                                           (i0_in_in_in + 4 /
                                                            4 * 4) + 4 % 4 /
                                                           4 * 4 + 4 / 4 * 4)))
                                                        )))), i1]
                                        for i0_in_in_in in seq(
                                                0, 4 % 4 % 4 % 4):
                                            Out[12 + 0 + 4 * (
                                                4 * i0_in_in_out +
                                                (4 * i0_in_in_out_1 +
                                                 (4 * i0_in_in_out_2 +
                                                  (4 * i0_in_in_out_3 +
                                                   (4 * i0_in_in_out_4 +
                                                    (4 * i0_in_in_out_5 +
                                                     (i0_in_in_in + 4 % 4 % 4 /
                                                      4 * 4 + 4 % 4 / 4 * 4 +
                                                      4 / 4 * 4))))))
                                            ), i1] = OutStaged[
                                                12 +
                                                0 +
                                                4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (i0_in_in_in + 4 % 4 %
                                                       4 / 4 * 4 + 4 % 4 / 4 *
                                                       4 + 4 / 4 * 4))))))),
                                                i1]
                                            Out[12 + 1 + 4 * (
                                                4 * i0_in_in_out +
                                                (4 * i0_in_in_out_1 +
                                                 (4 * i0_in_in_out_2 +
                                                  (4 * i0_in_in_out_3 +
                                                   (4 * i0_in_in_out_4 +
                                                    (4 * i0_in_in_out_5 +
                                                     (i0_in_in_in + 4 % 4 % 4 /
                                                      4 * 4 + 4 % 4 / 4 * 4 +
                                                      4 / 4 * 4))))))
                                            ), i1] = OutStaged[
                                                12 +
                                                1 +
                                                4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (i0_in_in_in + 4 % 4 %
                                                       4 / 4 * 4 + 4 % 4 / 4 *
                                                       4 + 4 / 4 * 4))))))),
                                                i1]
                                            Out[12 + 2 + 4 * (
                                                4 * i0_in_in_out +
                                                (4 * i0_in_in_out_1 +
                                                 (4 * i0_in_in_out_2 +
                                                  (4 * i0_in_in_out_3 +
                                                   (4 * i0_in_in_out_4 +
                                                    (4 * i0_in_in_out_5 +
                                                     (i0_in_in_in + 4 % 4 % 4 /
                                                      4 * 4 + 4 % 4 / 4 * 4 +
                                                      4 / 4 * 4))))))
                                            ), i1] = OutStaged[
                                                12 +
                                                2 +
                                                4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (i0_in_in_in + 4 % 4 %
                                                       4 / 4 * 4 + 4 % 4 / 4 *
                                                       4 + 4 / 4 * 4))))))),
                                                i1]
                                            Out[12 + 3 + 4 * (
                                                4 * i0_in_in_out +
                                                (4 * i0_in_in_out_1 +
                                                 (4 * i0_in_in_out_2 +
                                                  (4 * i0_in_in_out_3 +
                                                   (4 * i0_in_in_out_4 +
                                                    (4 * i0_in_in_out_5 +
                                                     (i0_in_in_in + 4 % 4 % 4 /
                                                      4 * 4 + 4 % 4 / 4 * 4 +
                                                      4 / 4 * 4))))))
                                            ), i1] = OutStaged[
                                                12 +
                                                3 +
                                                4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (4 * i0_in_in_out_5 +
                                                      (i0_in_in_in + 4 % 4 %
                                                       4 / 4 * 4 + 4 % 4 / 4 *
                                                       4 + 4 / 4 * 4))))))),
                                                i1]
                                    for i0_in_in_in in seq(0, 4 % 4):
                                        Out[12 + 0 + 4 * (
                                            4 * i0_in_in_out +
                                            (4 * i0_in_in_out_1 +
                                             (4 * i0_in_in_out_2 +
                                              (4 * i0_in_in_out_3 +
                                               (4 * i0_in_in_out_4 +
                                                (i0_in_in_in + 4 / 4 * 4)))))),
                                            i1] = OutStaged[
                                                12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (i0_in_in_in + 4 / 4 * 4))
                                                    )))), i1]
                                        Out[12 + 1 + 4 * (
                                            4 * i0_in_in_out +
                                            (4 * i0_in_in_out_1 +
                                             (4 * i0_in_in_out_2 +
                                              (4 * i0_in_in_out_3 +
                                               (4 * i0_in_in_out_4 +
                                                (i0_in_in_in + 4 / 4 * 4)))))),
                                            i1] = OutStaged[
                                                12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (i0_in_in_in + 4 / 4 * 4))
                                                    )))), i1]
                                        Out[12 + 2 + 4 * (
                                            4 * i0_in_in_out +
                                            (4 * i0_in_in_out_1 +
                                             (4 * i0_in_in_out_2 +
                                              (4 * i0_in_in_out_3 +
                                               (4 * i0_in_in_out_4 +
                                                (i0_in_in_in + 4 / 4 * 4)))))),
                                            i1] = OutStaged[
                                                12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (i0_in_in_in + 4 / 4 * 4))
                                                    )))), i1]
                                        Out[12 + 3 + 4 * (
                                            4 * i0_in_in_out +
                                            (4 * i0_in_in_out_1 +
                                             (4 * i0_in_in_out_2 +
                                              (4 * i0_in_in_out_3 +
                                               (4 * i0_in_in_out_4 +
                                                (i0_in_in_in + 4 / 4 * 4)))))),
                                            i1] = OutStaged[
                                                12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (4 * i0_in_in_out_2 +
                                                   (4 * i0_in_in_out_3 +
                                                    (4 * i0_in_in_out_4 +
                                                     (i0_in_in_in + 4 / 4 * 4))
                                                    )))), i1]
                                for i0_in_in_in in seq(0, 4 % 4):
                                    Out[12 + 0 + 4 *
                                        (4 * i0_in_in_out +
                                         (4 * i0_in_in_out_1 +
                                          (4 * i0_in_in_out_2 +
                                           (4 * i0_in_in_out_3 +
                                            (i0_in_in_in + 4 / 4 * 4))))),
                                        i1] = OutStaged[
                                            12 + 0 + 4 *
                                            (4 * i0_in_in_out +
                                             (4 * i0_in_in_out_1 +
                                              (4 * i0_in_in_out_2 +
                                               (4 * i0_in_in_out_3 +
                                                (i0_in_in_in + 4 / 4 * 4))))),
                                            i1]
                                    Out[12 + 1 + 4 *
                                        (4 * i0_in_in_out +
                                         (4 * i0_in_in_out_1 +
                                          (4 * i0_in_in_out_2 +
                                           (4 * i0_in_in_out_3 +
                                            (i0_in_in_in + 4 / 4 * 4))))),
                                        i1] = OutStaged[
                                            12 + 1 + 4 *
                                            (4 * i0_in_in_out +
                                             (4 * i0_in_in_out_1 +
                                              (4 * i0_in_in_out_2 +
                                               (4 * i0_in_in_out_3 +
                                                (i0_in_in_in + 4 / 4 * 4))))),
                                            i1]
                                    Out[12 + 2 + 4 *
                                        (4 * i0_in_in_out +
                                         (4 * i0_in_in_out_1 +
                                          (4 * i0_in_in_out_2 +
                                           (4 * i0_in_in_out_3 +
                                            (i0_in_in_in + 4 / 4 * 4))))),
                                        i1] = OutStaged[
                                            12 + 2 + 4 *
                                            (4 * i0_in_in_out +
                                             (4 * i0_in_in_out_1 +
                                              (4 * i0_in_in_out_2 +
                                               (4 * i0_in_in_out_3 +
                                                (i0_in_in_in + 4 / 4 * 4))))),
                                            i1]
                                    Out[12 + 3 + 4 *
                                        (4 * i0_in_in_out +
                                         (4 * i0_in_in_out_1 +
                                          (4 * i0_in_in_out_2 +
                                           (4 * i0_in_in_out_3 +
                                            (i0_in_in_in + 4 / 4 * 4))))),
                                        i1] = OutStaged[
                                            12 + 3 + 4 *
                                            (4 * i0_in_in_out +
                                             (4 * i0_in_in_out_1 +
                                              (4 * i0_in_in_out_2 +
                                               (4 * i0_in_in_out_3 +
                                                (i0_in_in_in + 4 / 4 * 4))))),
                                            i1]
                            for i0_in_in_in in seq(0, 4 % 4):
                                Out[12 + 0 + 4 *
                                    (4 * i0_in_in_out +
                                     (4 * i0_in_in_out_1 +
                                      (4 * i0_in_in_out_2 +
                                       (i0_in_in_in + 4 / 4 * 4)))),
                                    i1] = OutStaged[
                                        12 + 0 + 4 *
                                        (4 * i0_in_in_out +
                                         (4 * i0_in_in_out_1 +
                                          (4 * i0_in_in_out_2 +
                                           (i0_in_in_in + 4 / 4 * 4)))), i1]
                                Out[12 + 1 + 4 *
                                    (4 * i0_in_in_out +
                                     (4 * i0_in_in_out_1 +
                                      (4 * i0_in_in_out_2 +
                                       (i0_in_in_in + 4 / 4 * 4)))),
                                    i1] = OutStaged[
                                        12 + 1 + 4 *
                                        (4 * i0_in_in_out +
                                         (4 * i0_in_in_out_1 +
                                          (4 * i0_in_in_out_2 +
                                           (i0_in_in_in + 4 / 4 * 4)))), i1]
                                Out[12 + 2 + 4 *
                                    (4 * i0_in_in_out +
                                     (4 * i0_in_in_out_1 +
                                      (4 * i0_in_in_out_2 +
                                       (i0_in_in_in + 4 / 4 * 4)))),
                                    i1] = OutStaged[
                                        12 + 2 + 4 *
                                        (4 * i0_in_in_out +
                                         (4 * i0_in_in_out_1 +
                                          (4 * i0_in_in_out_2 +
                                           (i0_in_in_in + 4 / 4 * 4)))), i1]
                                Out[12 + 3 + 4 *
                                    (4 * i0_in_in_out +
                                     (4 * i0_in_in_out_1 +
                                      (4 * i0_in_in_out_2 +
                                       (i0_in_in_in + 4 / 4 * 4)))),
                                    i1] = OutStaged[
                                        12 + 3 + 4 *
                                        (4 * i0_in_in_out +
                                         (4 * i0_in_in_out_1 +
                                          (4 * i0_in_in_out_2 +
                                           (i0_in_in_in + 4 / 4 * 4)))), i1]
                        for i0_in_in_in in seq(0, 4 % 4):
                            Out[12 + 0 + 4 * (4 * i0_in_in_out +
                                              (4 * i0_in_in_out_1 +
                                               (i0_in_in_in + 4 / 4 * 4))),
                                i1] = OutStaged[12 + 0 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (i0_in_in_in + 4 / 4 * 4))),
                                                i1]
                            Out[12 + 1 + 4 * (4 * i0_in_in_out +
                                              (4 * i0_in_in_out_1 +
                                               (i0_in_in_in + 4 / 4 * 4))),
                                i1] = OutStaged[12 + 1 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (i0_in_in_in + 4 / 4 * 4))),
                                                i1]
                            Out[12 + 2 + 4 * (4 * i0_in_in_out +
                                              (4 * i0_in_in_out_1 +
                                               (i0_in_in_in + 4 / 4 * 4))),
                                i1] = OutStaged[12 + 2 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (i0_in_in_in + 4 / 4 * 4))),
                                                i1]
                            Out[12 + 3 + 4 * (4 * i0_in_in_out +
                                              (4 * i0_in_in_out_1 +
                                               (i0_in_in_in + 4 / 4 * 4))),
                                i1] = OutStaged[12 + 3 + 4 *
                                                (4 * i0_in_in_out +
                                                 (4 * i0_in_in_out_1 +
                                                  (i0_in_in_in + 4 / 4 * 4))),
                                                i1]
                    for i0_in_in_in in seq(0, 4 % 4):
                        Out[12 + 0 + 4 * (4 * i0_in_in_out +
                                          (i0_in_in_in + 4 / 4 * 4)),
                            i1] = OutStaged[12 + 0 + 4 *
                                            (4 * i0_in_in_out +
                                             (i0_in_in_in + 4 / 4 * 4)), i1]
                        Out[12 + 1 + 4 * (4 * i0_in_in_out +
                                          (i0_in_in_in + 4 / 4 * 4)),
                            i1] = OutStaged[12 + 1 + 4 *
                                            (4 * i0_in_in_out +
                                             (i0_in_in_in + 4 / 4 * 4)), i1]
                        Out[12 + 2 + 4 * (4 * i0_in_in_out +
                                          (i0_in_in_in + 4 / 4 * 4)),
                            i1] = OutStaged[12 + 2 + 4 *
                                            (4 * i0_in_in_out +
                                             (i0_in_in_in + 4 / 4 * 4)), i1]
                        Out[12 + 3 + 4 * (4 * i0_in_in_out +
                                          (i0_in_in_in + 4 / 4 * 4)),
                            i1] = OutStaged[12 + 3 + 4 *
                                            (4 * i0_in_in_out +
                                             (i0_in_in_in + 4 / 4 * 4)), i1]
                for i0_in_in_in in seq(0, 1 % 4):
                    Out[12 + 0 + 4 * (i0_in_in_in + 1 / 4 * 4),
                        i1] = OutStaged[12 + 0 + 4 * (i0_in_in_in + 1 / 4 * 4),
                                        i1]
                    Out[12 + 1 + 4 * (i0_in_in_in + 1 / 4 * 4),
                        i1] = OutStaged[12 + 1 + 4 * (i0_in_in_in + 1 / 4 * 4),
                                        i1]
                    Out[12 + 2 + 4 * (i0_in_in_in + 1 / 4 * 4),
                        i1] = OutStaged[12 + 2 + 4 * (i0_in_in_in + 1 / 4 * 4),
                                        i1]
                    Out[12 + 3 + 4 * (i0_in_in_in + 1 / 4 * 4),
                        i1] = OutStaged[12 + 3 + 4 * (i0_in_in_in + 1 / 4 * 4),
                                        i1]