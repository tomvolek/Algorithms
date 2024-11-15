cc := gcc
NVCC := nvcc 
CFLAGS := -Wall -Wextra
CUDAFLAGS := -arch=sm_75 -lcudart -lcublas

SRC_DIR := src 
INCLUDE_DIR := include 
OBJ_DIR := obj
BIN_DIR := bin 

SRC := $(wildcard $(SRC_DIR)/*.c)
CUDA_SRC := $(wildcard $(SRC_DIR)/*.cu)
OBJ := $patsubst $(SRC_DIR)/*.c, $(OBJ_DIR)/*.o, $(SRC))
CUDA_OBJ := $patsubst $(SRC_DIR)/*.cu, $(OBJ_DIR)/%.cu.o, $(CUDA_SRC))
TARGET := $(BIN_DIR)/program

DEPS := $(wildcard $(INCLUDE_DIR)/*.h) $(wildcard $(SRC_DIR)/*.h)
CUDA_DEPS := $(wildcard $(INCLUDE_DIR)/*.cuh) $(wildcard $(SRC_DIR)/*.cuh)

.PHONY: all clean 

all: $(TARGET)

$(TARGET): $(OBJ) $(CUDA_OBJ)
			$(NVCC) $(CUDAFLAGS) $^ -o $@

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(DEPS)
		@mkdir -p $(@D)
		$(CC) $(CFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

$(OBJ_DIR)/%.cu.o: $(SRC_DIR)/%.cu $(CUDA_DEPS)
		@mkdir -p $(@D)
		$(NVCC) $(CUDAFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

clean:
		rm -rf $(ONJ_DIR)/*.0 $OBJ_DIR)/*.cu.o $(TARGET)
	