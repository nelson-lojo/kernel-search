#include "generated_ker.h"



#include <stdio.h>
#include <stdlib.h>



// generated_operation(
//     In : f32[16, 16] @DRAM,
//     Weights : f32[16, 16] @DRAM,
//     Out : f32[16, 16] @DRAM
// )
//*
void generated_operation(const elem_t* In, const elem_t* Weights, elem_t* Out ) {
for (int_fast32_t i = 0; i < 16; i++) {
  for (int_fast32_t j = 0; j < 16; j++) {
    for (int_fast32_t k = 0; k < 16; k++) {
      Out[i * 16 + j] += In[i * 16 + k] * Weights[k * 16 + j];
    }
  }
}
}
/*/

void generated_operation(const elem_t *In, const elem_t *Weights, elem_t *Out) {
  // printf("Calculate the scratchpad addresses of all our matrices\n");
  // printf("  Note: The scratchpad is \"row-addressed\", where each address contains one matrix row\n");
  size_t In_sp_addr = 0;
  size_t Out_sp_addr = DIM;
  size_t Weights_sp_addr = 2*DIM;

  // printf("Move \"In\" matrix from main memory into Gemmini's scratchpad\n");
  gemmini_config_ld(DIM * sizeof(elem_t));
  gemmini_config_st(DIM * sizeof(elem_t));
  gemmini_mvin(In, In_sp_addr);

  // printf("Move \"Identity\" matrix from main memory into Gemmini's scratchpad\n");
  gemmini_mvin(Weights, Weights_sp_addr);

  // printf("Multiply \"In\" matrix with \"Identity\" matrix with a bias of 0\n");
  gemmini_config_ex(OUTPUT_STATIONARY, 0, 0);
  gemmini_preload_zeros(Out_sp_addr);
  gemmini_compute_preloaded(In_sp_addr, Weights_sp_addr);

  // printf("Move \"Out\" matrix from Gemmini's scratchpad into main memory\n");
  gemmini_config_st(DIM * sizeof(elem_t));
  gemmini_mvout(Out, Out_sp_addr);

  // printf("Fence till Gemmini completes all memory operations\n");
  gemmini_fence();
}
// */
aws-c-auth aws-c-cal aws-c-common aws-c-compression aws-c-event-stream aws-c-http aws-c-io aws-c-mqtt aws-c-s3 aws-c-sdkutils aws-checksums aws-sam-translator aws-xray-sdk  awscli     awscrt     azure-core azure-identity 
// generated_operation_scheduled(
//     In : f32[16, 16] @DRAM,
//     Weights : f32[16, 16] @DRAM,
//     Out : f32[16, 16] @DRAM
// )
void generated_operation_scheduled( void *ctxt, const float* In, const float* Weights, float* Out ) {
for (int_fast32_t k = 0; k < 16; k++) {
  for (int_fast32_t i = 0; i < 16; i++) {
    for (int_fast32_t jo = 0; jo < 2; jo++) {
      for (int_fast32_t ji = 0; ji < 8; ji++) {
        Out[i * 16 + ji + 8 * jo] += In[i * 16 + k] * Weights[k * 16 + ji + 8 * jo];
      }
    }
  }
}
}