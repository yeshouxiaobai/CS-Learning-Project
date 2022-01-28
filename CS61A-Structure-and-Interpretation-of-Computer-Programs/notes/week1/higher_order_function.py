def identity(x):
    return x


def square(x):
    return x*x


def cube(x):
    return x*x*x


def summation(n, term):
    """Return term(0) + term(1) + ... + term(n)."""
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def pi_term(x):
    return 8 / ((4*x-3)*(4*x-1))


def pi_sum(n):
    """Return approximate value of pi after n iteration.

    Usage: print("Pi is:", pi_sum(1e6))
    """
    return summation(n, pi_term)


def sum_naturals(n):
    """Return sum of 0, 1, 2, ..., n.

    >>> sum_naturals(100)
    5050
    """
    return summation(n, identity)


def sum_square(n):
    """Return sum of square(0), square(1), ..., square(n).
    >>> sum_square(10)
    385
    """
    return summation(n, square)


def sum_cube(n):
    """Return sum of cube(0), cube(1), ..., cube(n).
    >>> sum_cube(10)
    3025
    """
    return summation(n, cube)


def imporve(update, good_enough, guess=1):
    """Retrun a guess which is good enough.

    This function first makes a guess(default is 1),
    then uses guess = update(guess) to iterate it,
    until good_enough(guess) return True.
    """
    while not good_enough(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance


def golden():
    """Return the golden ratio.

    >>> from math import sqrt
    >>> phi = 1/2 + sqrt(5)/2
    >>> approx_eq(phi, golden())
    True
    """
    def golden_update(guess):
        return 1/guess + 1

    def square_close_to_successor(guess):
        return approx_eq(guess*guess, guess+1)
    return imporve(golden_update, square_close_to_successor)


def sqrt(a):
    """Return the sqrt of a.

    >>> approx_eq(4.0, sqrt(16))
    True
    >>> approx_eq(1.414, sqrt(2), tolerance=0.01)
    True
    """
    def average(x, y):
        return (x+y)/2

    def sqrt_update(x):
        return average(x, a/x)

    def sqrt_close(x):
        return approx_eq(x*x, a)
    return imporve(sqrt_update, sqrt_close)


def newton_update(f, df):
    """Return newton update function of f.

    f is a function. df is the derivation of f.
    """
    def update(x):
        return x - f(x) / df(x)
    return update


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return imporve(newton_update(f, df), near_zero)


def square_root_newton(a):
    """Return square root of a.

    Usage:
    square_root_newton(a)
    """
    def f(x):
        return x * x - a

    def df(x):
        return 2 * x
    return find_zero(f, df)


def power(x, n):
    """Return x * x * x * ... * x for x repeated n times."""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product


def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a

    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)
