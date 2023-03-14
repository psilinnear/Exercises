# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:41:37 2023

@author: rensmo_l
"""

## Test the animals package
# Import classes from your brand new package
#import animals

#m = animals.Mammals()
#m.printMembers()

#b = animals.Birds()
#b.printMembers()

#f = animals.Fish()
#f.printMembers()

#%% 

import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()