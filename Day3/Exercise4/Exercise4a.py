# -*- coding: utf-8 -*-
"""
a) Write a simple MPI scrip mpi_ranks.py that prints the rank
    of the different processes when running
    mpirun python mpi_ranks.py

"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("hello world from process ", rank)

# Manged to execute this using mpiexec -n 5 python Exercise4a.py
# Got the following result

# hello world from process  4
# hello world from process  0
# hello world from process  3
# hello world from process  2
# hello world from process  1

