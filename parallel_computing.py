import numpy as np
import cupy as cp
import time


start_time = time.time()
myvar_cpu = np.ones((800, 800, 800))
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
myvar_gpu = cp.ones((800, 800, 800))
end_time = time.time()
print(end_time - start_time)
