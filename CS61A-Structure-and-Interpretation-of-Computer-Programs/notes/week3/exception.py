# assert statement can raise AssertionError
# `assert <expression>, <string>`

# raise statements
# `raise <expression>`
# <expression> must evaluate to a subclass of BaseException
# or an instance of one.
# =======================
# TypeError
# NameError
# KeyError
# RuntimeError
# =======================
# We can construct all these errors.
# `raise TypeError('Bad argument')`
# `abs('hello')`
# `hello`
# `{}['hello']`

# Try statement
try:
    x = 1/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    x = 0

def invert(x):
    y = 1/x
    print('Never printed if x is 0')
    return y

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled', e)
        return 0

# Examples using try statement.
from operator import mul, truediv, add

    
def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.
    E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).
    
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    for x in s:
        initial = f(initial, x)
    return initial

def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.
    E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).
    
    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    """
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))

def divide_all(n, ds):
    # reduce should have no knowledge about divide_all,
    # so try statement is here.
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')
