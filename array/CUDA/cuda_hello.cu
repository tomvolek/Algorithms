// System includes
#include <assert.h>
#include <stdint.h>
#include <stdio.h>

// CUDA runtime
//#include <cuda_runtime.h>

// helper functions and utilities to work with CUDA
//#include <helper_cuda.h>
//#include <helper_functions.h>


// kernel definition 
__global__ void cuda_hello() { 
        printf("Hellow World from GPU");

}

int main() { 
    cuda_hello<<<1,1>>>();
    retirn 0;
}





