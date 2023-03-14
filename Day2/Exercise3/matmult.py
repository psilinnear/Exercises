import time

# get the start time
st = time.time()

# Program to multiply two matrices using nested loops
import random

N = 250

# NxN matrix
X = []
for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
result = []
for i in range(N):
    result.append([0] * (N+1))

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)
    
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


# In this section, you should get more familiar with code 
# profiling, in particular with the tools cProfile, line_profiler.
# Have a look at slides from this morning's session to understand 
# what they are doing and when you should use them. 
# Try out profiling both from the command line and using
# interactive python (e.g. jupyter notebook). 
# If you get Command not found when running kernprof try
# searching for it in ~/.local/bin/kernprof. Alternatively
# install it using Anaconda/conda (e.g. conda install 
# line_profiler).

# a) Investigate the performance of the matmult.py scripts. 
# In which line(s) of the script would you start optimizing 
# for speed? 

# The second for loop takes the longest, since it both
# append stuff 250 times, but also, in each loop uses the
# random function. 