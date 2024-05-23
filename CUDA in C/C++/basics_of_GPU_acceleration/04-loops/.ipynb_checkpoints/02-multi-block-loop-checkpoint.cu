#include <stdio.h>

/*
 * Refactor `loop` to be a CUDA Kernel. The new kernel should
 * only do the work of 1 iteration of the original loop.
 */
 
 
__global__ void GPU_loop() {

    int block = blockIdx.x;
    int thread = threadIdx.x;
    
    printf("This is core number %d\n", block*blockDim.x + thread);

}

void loop(int N)
{
  for (int i = 0; i < N; ++i)
  {
    printf("This is iteration number %d\n", i);
  }
}

int main()
{
  /*
   * When refactoring `loop` to launch as a kernel, be sure
   * to use the execution configuration to control how many
   * "iterations" to perform.
   *
   * For this exercise, be sure to use more than 1 block in
   * the execution configuration.
   */

  int N = 10;
  //loop(N);
  
  int numBlocksToUse = 2;
  
  GPU_loop <<<numBlocksToUse,N/numBlocksToUse>>>();
  cudaDeviceSynchronize();
}
