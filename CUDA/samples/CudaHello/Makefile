# Location of the CUDA Toolkit
CUDAPATH = /usr/local/cuda
# NVCC is path to nvcc. Here it is assumed that /usr/local/cuda is on one's PATH.
NVCC = /usr/local/cuda/bin/nvcc

NVCCFLAGS = -I$(CUDAPATH)/include
LFLAGS = -L$(CUDAPATH)/lib64 -lcuda -lcudart -lm

cuda_hello:
	$(NVCC) $(NVCCFLAGS) $(LFLAGS) -o cuda_hello cuda_hello.cu