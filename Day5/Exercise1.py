#%% a+b) Define matrix A and vector b
A = [[1, -2, 3], [4, 5, 6], [7, 1, 9]]
b = [1, 2, 3]

#%%  c) Solve the linear system of equations Ax = b
from scipy.linalg import solve

sol = solve(A, b)
print(sol)

#%% d) Check that your solution is correct by plugging it into the equation

test = A*sol
print(test)

# Shows me very small numbers instead of zero

#%% e) Repeat steps a-d using a random 3x3 matrix instead of b
import numpy as np

b = np.random.rand(3, 3)
sol = solve(A,b)
print(sol)

#%% f) Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors
from scipy.linalg import eig

eigenvalues, eigenvectors = eig(A)

print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

#%% g) Calculate the inverse, determinant of A

from scipy.linalg import inv, det

A_inv = inv(A)
A_det = det(A)

print("Inverse of A:")
print(A_inv)
print("Determinant of A:")
print(A_det)

#%%  h) Calculate the norm of A with different orders

from scipy.linalg import norm

# 1-norm of A
norm_1 = norm(A, 1)

# 2-norm of A
norm_2 = norm(A, 2)

# Infinity norm of A
norm_inf = norm(A, np.inf)

print("1-norm of A:")
print(norm_1)
print("2-norm of A:")
print(norm_2)
print("Infinity norm of A:")
print(norm_inf)

#%% i) Create a discrete random variable with poissonian distribution and plot its 
# probability mass function (PMF), cummulative distribution function (CDF) and a histogram
#  of 1000 random realizations of the variable

import matplotlib.pyplot as plt
from scipy.stats import poisson

# Create a Poisson random variable with lambda = 3
X = poisson(mu=3)

# Plot the PMF
x_values = np.arange(0, 11)
pmf = X.pmf(x_values)
plt.stem(x_values, pmf)
plt.title("Probability Mass Function (PMF)")
plt.xlabel("X")
plt.ylabel("P(X)")
plt.show()

# Plot the CDF
cdf = X.cdf(x_values)
plt.step(x_values, cdf)
plt.title("Cumulative Distribution Function (CDF)")
plt.xlabel("X")
plt.ylabel("P(X <= x)")
plt.show()

# Plot a histogram of 1000 random realizations
samples = X.rvs(size=1000)
plt.hist(samples, bins=11, density=True)
plt.title("Histogram of 1000 Realizations")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.show()

#%% j) Create a continuous random variable with normal distribution and plot its probability 
# mass function (PMF), cummulative distribution function (CDF) and a histogram of 1000 random 
# realizations of the variable

from scipy.stats import norm

# Create a normal random variable with mean = 0 and standard deviation = 1
X = norm()

# Plot the PDF
x_values = np.linspace(-5, 5, 1000)
pdf = X.pdf(x_values)
plt.plot(x_values, pdf)
plt.title("Probability Density Function (PDF)")
plt.xlabel("X")
plt.ylabel("f(X)")
plt.show()

# Plot the CDF
cdf = X.cdf(x_values)
plt.plot(x_values, cdf)
plt.title("Cumulative Distribution Function (CDF)")
plt.xlabel("X")
plt.ylabel("F(X)")
plt.show()

# Plot a histogram of 1000 random realizations
samples = X.rvs(size=1000)
plt.hist(samples, bins=50, density=True)
plt.title("Histogram of 1000 Realizations")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.show()

#%% k) c. Test if two sets of (independent) random data comes from the same distribution
# Hint: Have a look at the ttest_ind function
from scipy.stats import ttest_ind

# Generate two sets of independent random data with a normal distribution
data1 = norm.rvs(loc=0, scale=1, size=100)
data2 = norm.rvs(loc=1, scale=1, size=100)

# Perform the t-test and store the result in a variable
t_statistic, p_value = ttest_ind(data1, data2, equal_var=True)

# Print the result
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")
if p_value < 0.05:
    print("The two sets of data come from different distributions.")
else:
    print("The two sets of data come from the same distribution.")