from math import sqrt


def if_(c, t, f):
    if c():
        return t()
    return f()


def real_aqrt(x):
    """The real part of the square root of X."""
    return if_(lambda: x > 0, lambda: sqrt(x), lambda: 0.0)


print(real_aqrt(2))
print(real_aqrt(-2))


def my_print(something, ret):
    print(something)
    return ret


my_print(1, False) and my_print(2, True) or my_print(3, False)
