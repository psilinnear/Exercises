# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:20:10 2023

@author: rensmo_l
"""

class Fish:
	def __init__(self):
		# Create some member animals
		self.members =['Shark', 'Goldfish', 'Whale']
    
	def printMembers(self):
		print('Printing members of the Fish class')
		for member in self.members:
			print('\t%s' % member)