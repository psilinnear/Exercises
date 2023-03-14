import numpy as np

#%% a) Create a null vector of size 10 but the fifth value is 1

null_vector = np.zeros(10) # To create null vector
null_vector[4] = 1 # Change the fifth value to one
print(null_vector) # To see if it worked

#%% b) Create a vector with values ranging from 10 to 49

vector = np.arange(10,49+1) #assuming we only want integers between 10 and 49
print(vector)

#%% c) Reverse a vector, I use my previous vector

vector_reversed = vector[::-1]
print(vector_reversed)

#%% d) Create a 3x3 matrix with values ranging from 0 to 8

vector_for_matrix = np.arange(9)
matrix = vector_for_matrix.reshape((3,3))

print(matrix)

#%% e) Find indices of non-zero elements from [1,2,0,0,4,0]

vector_e = [1,2,0,0,4,0]
nonzero_indices = [i for i in range(len(vector_e)) if vector_e[i] != 0]

print(nonzero_indices)

#%% f) Create a random vector of size 30 and find the mean value

vector_f = np.random.rand(30) # Create the vector
mean_of_vector = np.mean(vector_f) # Calculate the mean

print(mean_of_vector)

#%% g) Create a 2d array with 1 on the border and 0 inside

length = 10 # Can change this to the length I want my vector to be
matrix_g = np.zeros((length,length))
matrix_g[0,:] = 1   # Change the upper row
matrix_g[:,-1] = 1  # Change the right side
matrix_g[:,0] = 1   # Change the left side
matrix_g[-1,:] = 1  # Change the lower row

print(matrix_g)

#%% h) Create a 8x8 matrix and fill it with a checkerboard pattern

matrix_h = np.zeros((8,8)) # Create the matrix
matrix_h[::2, ::2] = 1 # Create ones on every other row and every other column starting from 0
matrix_h[1::2, 1::2] = 1 # Create ones on every other row and every other column starting from 1
print(matrix_h)

#%% i) Create a 8x8 checkerboard using the tile function

small_checkerboard = np.array([[0,1], [1,0]])
big_checkerboard = np.tile(small_checkerboard, (4,4))

print(big_checkerboard)

#%% j) Given a 1D array, negate all elements which are between 3 and 8 in place

vector_j = np.arange(11)
for i in range(len(vector_j)):
    if 3<= vector_j[i] <=8:
        vector_j[i]=-vector_j[i]

print(vector_j)

#%% k) Create a random vector of size 10 and sort it

vector_k = np.random.random(10)
vector_k = np.sort(vector_k)

print(vector_k)

#%% l) Consider two random arrays A and B, check if they are equal

A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.sum(abs(A-B))

print(equal) # If they are equal the sum should be zero

#%% m) How to convert an integer (32bits) array into a float (32bits) in place

vector_m = np.arange(10, dtype=np.int32)
print(vector_m.dtype)

vector_m = vector_m.astype(np.float32)

print(vector_m.dtype)

#%% n) How to get the diagonal of a dot product

A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)

print(D)

