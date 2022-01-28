"""Our first Python source file."""
# filename: try_doctest.py
# use 'python -m doctest -v try_doctest.py' to tests this.

from operator import floordiv, mod

def divide_exact(n, d):
    """Return the quotient and remainder of divding N by D.
    
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

def absolute_value(x):
    """Return the absolute value of x.
    
    >>> absolute_value(1)
    1
    >>> absolute_value(0)
    0
    >>> absolute_value(-1)
    1
    """
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
    
def fib(n):
    """Compute the nth Fibonacci number, for N >= 1.
    
    >>> fib(1)
    1
    >>> fib(3)
    2
    >>> fib(10)
    55
    """
    pred, curr = 0, 1  # 0th and 1st Fibnoacci numbers
    k = 1              # curr is the kth Fibonacci number
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr
