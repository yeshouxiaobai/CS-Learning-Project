from operator import getitem
from math import gcd

pair = [1, 2]
getitem(pair, 0)
getitem(pair, 1)

# Rational arithmetic

def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    """Multiply rational number x and y."""
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def rationals_are_equal(x, y):
    """Return whether rational numbers x and y are equal."""
    return numer(x) * denom(y) == numer(y) * denom(x)    

def print_rational(x):
    """Print rational x."""
    print(numer(x), "/", denom(x))

# Constructor and selectors

# Version 1

# def rational(n, d):
#     """Construct a rational number that represents N/D."""
#     g = gcd(n, d)
#     return [n//g, d//g]

# def numer(x):
#     """Return the numerator of rational number X."""
#     return x[0]

# def denom(x):
#     """Return the denominator of rational number X."""
#     return x[1]

# Version 2

def rational(n, d):
    """Construct a rational number that represents N/D."""
    g = gcd(n, d)
    def select(name):
        if name == 'n':
            return n//g
        elif name == 'd':
            return d//g
    return select

def numer(x):
    """Return the numerator of rational number X."""
    return x('n')

def denom(x):
    """Return the denominator of rational number X."""
    return x('d')
