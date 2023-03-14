# -*- coding: utf-8 -*-
"""
Test of simple_math

"""

import simple_math 

def test_simple_add():
    assert simple_math.simple_add(1,2) == 3
    
def test_simple_sub():
    assert simple_math.simple_sub(1,1) == 0
    
def test_simple_mult():
    assert simple_math.simple_mult(1,1) == 1
    
def test_simple_div():
    assert simple_math.simple_div(1,1) == 1
    
def test_poly_first():
    assert simple_math.poly_first(1,1,1) == 2
    
def test_poly_second():
    assert simple_math.poly_second(1,1,1,1) == 3
    
    
    
    
# Got the following results

# ============================= test session starts =============================
# platform win32 -- Python 3.9.16, pytest-7.2.2, pluggy-1.0.0
# rootdir: C:\Users\rensmo_l\Documents\Advanced python programming\day4-bestpractices-2\Exercise1
# collected 6 items

# test_simple_math.py ......                                               [100%]

# ============================== 6 passed in 0.02s ==============================



