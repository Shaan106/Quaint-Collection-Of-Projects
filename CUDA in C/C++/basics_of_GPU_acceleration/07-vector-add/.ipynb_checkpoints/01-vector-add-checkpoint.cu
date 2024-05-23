#include <stdio.h>

void initWith(float num, float *a, int N)
{
  for(int i = 0; i < N; ++i)
  {
    a[i] = num;
  }
}

__global__ void initWith_GPU(float num, float *a, int N) {
    
    int gridIndex = threadIdx.x + blockIdx.x*blockDim.x;
    int strideSize = gridDim.x*blockDim.x;
    
    for (int i = gridIndex; i < N; i = i + strideSize) {
        a[i] = num;
    }
}

void addVectorsInto(float *result, float *a, float *b, int N)
{
  for(int i = 0; i < N; ++i)
  {
    result[i] = a[i] + b[i];
  }
}

__global__ void addVectorsInto_GPU(float *result, float *a, float *b, int N) {
    
    int gridIndex = threadIdx.x + blockIdx.x*blockDim.x;
    int strideSize = gridDim.x*blockDim.x;
     
    for (int i = gridIndex; i < N; i = i + strideSize) {
        result[i] = a[i] + b[i];
    }
    
}

void checkElementsAre(float target, float *array, int N)
{
  for(int i = 0; i < N; i++)
  {
    if(array[i] != target)
    {
      printf("FAIL: array[%d] - %0.0f does not equal %0.0f\n", i, array[i], target);
      exit(1);
    }
  }
  printf("SUCCESS! All values added correctly.\n");
}

int main()
{
  const int N = 2<<20;
  size_t size = N * sizeof(float);

  float *a;
  float *b;
  float *c;

  //a = (float *)malloc(size);
  //b = (float *)malloc(size);
  //c = (float *)malloc(size);
  
  cudaMallocManaged(&a, size);
  cudaMallocManaged(&b, size);
  cudaMallocManaged(&c, size);
    
  int numThreads = 1024;
  int numBlocks = 32;

  // initWith(3, a, N);
  // initWith(4, b, N);
  // initWith(0, c, N);
  
  initWith_GPU<<<numBlocks,numThreads>>>(3, a, N);
  initWith_GPU<<<numBlocks,numThreads>>>(4, b, N);
  initWith_GPU<<<numBlocks,numThreads>>>(0, c, N);
    
  cudaDeviceSynchronize();

  // addVectorsInto(c, a, b, N);
  addVectorsInto_GPU<<<numBlocks,numThreads>>>(c, a, b, N);
    
  cudaDeviceSynchronize();

  checkElementsAre(7, c, N);

  // free(a);
  // free(b);
  // free(c);
    
  cudaFree(a);
  cudaFree(b);
  cudaFree(c);
}
