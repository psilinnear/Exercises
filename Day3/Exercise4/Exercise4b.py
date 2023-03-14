# -*- coding: utf-8 -*-
"""
b) Write a small script mpi_sum.py which calculates the sum 
    over all ranks and prints the results from the process
    with rank 0

"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    print("This is rank 0") # Prints the results from the process with rank 0
    
sum_of_ranks = comm.allreduce(rank, op=MPI.SUM)
print(sum_of_ranks) # The sum of ranks is always the same?
    




