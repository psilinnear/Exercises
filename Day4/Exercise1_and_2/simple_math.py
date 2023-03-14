"""

This code creates functions of some easy mathematic tools

This is in line according to the following exercises:
a) Write some meaningful docstrings for the simple_math.py module, e.g
    following the numpy_doc standard
    
b) Create a documentation html page for the simple_math.py
    using Sphinx

"""

def simple_add(a,b):
    """
    Parameters
    ----------
    a : float or int
        One of the numbers to be added
    b : float or int
        One of the numbers to be added

    Returns
    -------
    Float or inte
        Returns result of adding A and B

    """
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

