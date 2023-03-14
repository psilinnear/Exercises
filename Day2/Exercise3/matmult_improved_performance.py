# Previous time: 3.45 s
# To improve the code I use numpy instead of appending to a 
# vector all the time. Numpy has its own function random, so I 
# only have to import numpy, and no longer have to import 
# random

# The time was decreased to 0.0983 s

import time

# get the start time
st = time.time()

import numpy as np

N = 250

# NxN matrix
X = np.random.randint(0, 100, size=(N, N))

# Nx(N+1) matrix
Y = np.random.randint(0, 100, size=(N, N+1))

# result is Nx(N+1)
result = np.zeros((N, N+1))

# perform matrix multiplication
result = np.dot(X, Y)

for r in result:
    print(r)
    
    et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')