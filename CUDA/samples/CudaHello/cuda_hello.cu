
// System includes
#include <stdio.h>
#include <assert.h>
#include <unistd.h>

// CUDA runtime
#include <cuda_runtime.h>
#include <cuda_profiler_api.h>


// kernel definition 

__global__ void veectorAdd(int * a, int *b, int *c) { 

    int i = threadIdx.x;
    c[i] = a[i] + b[i];
    printf("inside kernel code\n") ; 
    return;

}

int main() { 
    int a[]= { 1,2,3};
    int b[] = {4,5,6};
    int c[sizeof(a) /sizeof(int)] = {0};

int *cudaA = 0; 
int *cudaB = 0;
int *cudaC = 0; 

cudaMalloc(&cudaA, sizeof(a));
cudaMalloc(&cudaB, sizeof(a));
cudaMalloc(&cudaC, sizeof(a));

//allcoate memory
cudaMemcpy(cudaA,a,sizeof(a), cudaMemcpyHostToDevice);
cudaMemcpy(cudaB,b,sizeof(b), cudaMemcpyHostToDevice);
cudaMemcpy(cudaC,c,sizeof(c), cudaMemcpyHostToDevice);

printf("Inside main\n");

    veectorAdd<<<1,sizeof(a) /sizeof(int)>>>(cudaA,cudaB, cudaC);
    cudaMemcpy (c,cudaC,sizeof(c),cudaMemcpyDeviceToHost);
    return 0 ;
}





