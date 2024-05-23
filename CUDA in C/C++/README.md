# What is this?

These are my personal notes/braindump from when I was learning CUDA programming. My notes are mostly in the jupyter notebook, but some helpful code snippets are also in the README.

Resources I'm learning from:

- NVIDIA CUDA docs: https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html

# CUDA cheatsheet

### Kernel declaration

Create a kernel function that will run on the GPU. The `__global__` keyword is a CUDA specifier that indicates that this function will run on the GPU and can be called from the host.

``` cpp
__global__ void GPUFunction()
{
  printf("This function is defined to run on the GPU.\n");
}
```
### Calling kernel

To call a kernel function from the host, use the following syntax. The `<<<...>>>` syntax is specific to CUDA and is used to specify the number of blocks and threads that will be used to run the kernel.

```cpp
	//n_blocks, n_threads
GPUFunction<<<1, 1>>>();
```

### CUDA Synchronization

Syncrhonize the CPU with the GPU to ensure that all the kernels have finished running before continuing with the CPU code.

```cpp
cudaDeviceSynchronize();
```

### Mapping cuda indexes into index of data

Common way of mapping indexes of data to CUDA threads and blocks.

``` cpp
int data_index = threadIdx.x + blockIdx.x * blockDim.x;
```

### Computing number of needed blocks for data
``` cpp
int number_of_blocks = (N + threads_per_block - 1) / threads_per_block;
```

### Manging shared memory

Using shared memory in CUDA kernels to speed up computation, CUDA malloc managed automatically deals with this, but using prefetching can significantly speed up the computation (in sections below).

``` cpp
int N = 100;
int *a;
size_t size = N * sizeof(int);
cudaMallocManaged(&a, size);
cudaFree(a);
```

### Grid stride loop

For data that is larger than the number of threads available in device, using a grid stride loop will ensure computation of all elements.

``` cpp
int idx = blockIdx.x * blockDim.x + threadIdx.x;
int stride = gridDim.x * blockDim.x;

for (int i = idx; i < N; i += stride)
{
	a[i] = a[i]; //do work
}
```

### Shared memory management error handling
``` cpp
cudaError_t err;
err = cudaMallocManaged(&a, N);                    	// Assume the existence of `a` and `N`.

if (err != cudaSuccess)                           	// `cudaSuccess` is provided by CUDA.
{
	printf("Error: %s\n", cudaGetErrorString(err)); // `cudaGetErrorString` is provided by CUDA.
}

```

### Kernel running error handling
``` cpp
someKernel<<<1, -1>>>();  // -1 is not a valid number of threads.

cudaError_t err;
err = cudaGetLastError(); // `cudaGetLastError` will return the error from above.
if (err != cudaSuccess)
{
	printf("Error: %s\n", cudaGetErrorString(err));
}
```

### General CUDA error handling function
``` cpp
inline cudaError_t checkCuda(cudaError_t result)
{
	if (result != cudaSuccess) {
		fprintf(stderr, "CUDA Runtime Error: %s\n", cudaGetErrorString(result));
		assert(result == cudaSuccess);
	}
	return result;
}
```

### Profiling and Optimizing 
``` cpp
// in the terminal
!nvcc -o iteratively-optimized-vector-add 01-vector-add/01-vector-add.cu -run

!nsys profile --stats=true ./iteratively-optimized-vector-add
```

### Device information
``` cpp
#include <stdio.h>

int main()
{


  /*
   * Device ID is required first to query the device.
   */

  int deviceId;
  cudaGetDevice(&deviceId);

  cudaDeviceProp props;
  cudaGetDeviceProperties(&props, deviceId);

  /*
   * `props` now contains several properties about the current device.
   */

  int computeCapabilityMajor = props.major;
  int computeCapabilityMinor = props.minor;
  int multiProcessorCount = props.multiProcessorCount;
  int warpSize = props.warpSize;

  printf("Device ID: %d\nNumber of SMs: %d\nCompute Capability Major: %d\nCompute Capability Minor: %d\nWarp Size: %d\n", deviceId, multiProcessorCount, computeCapabilityMajor, computeCapabilityMinor, warpSize);
}
```
then run the following in the terminal
``` bash
nvcc -o get-device-properties 04-device-properties/01-get-device-properties.cu -run
```

### Memory Prefetching
One of the major performance bottlenecks in GPU programming is the time it takes to transfer data between the host and device. One way to mitigate this bottleneck is to use memory prefetching. This allows the GPU to start transferring the data before it is actually needed, which can help to hide the latency of the data transfer.

``` cpp
int deviceId;
cudaGetDevice(&deviceId);                                         // The ID of the currently active GPU device.

cudaMemPrefetchAsync(pointerToSomeUMData, size, deviceId);        // Prefetch to GPU device.
cudaMemPrefetchAsync(pointerToSomeUMData, size, cudaCpuDeviceId); // Prefetch to host. `cudaCpuDeviceId` is a built-in CUDA variable.
```