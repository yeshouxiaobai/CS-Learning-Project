# assert
def fact(x):
    assert isinstance(x, int)
    assert x >= 0
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)
    
def half_fact(x):
    # When using assert, we can find the error in
    # this function.
    return fact(x/2)

# testing: doctests
def fib(n):
    """Fibonacci
    
    >>> fib(2)
    1
    >>> fib(10)
    55
    """
    a, b, cnt = 0, 1, 0
    while cnt < n:
        a, b, cnt = b, a+b, cnt+1
    return a

# print to debug
# `print('x =', x)`

# interactive debugging: REPL
# `python -i file.py`

# interactive debugging: PythonTutor
# tutor.cs61a.org

# Error Type and Error Message Patterns
# SyntaxError
# IndentationError
# TypeError
# NameError or UnboundLocalError

# Traceback

# def f(x):
#     1/0
# def g(x):
#     f(x)
# def h(x):
#     g(x)
# print(h(2))

# Traceback (most recent call last):
#   File "week3\debugging.py", line 51, in <module>
#     print(h(2))
#   File "week3\debugging.py", line 50, in h
#     g(x)
#   File "week3\debugging.py", line 48, in g
#     f(x)
#   File "week3\debugging.py", line 46, in f
#     1/0
# ZeroDivisionError: division by zero
