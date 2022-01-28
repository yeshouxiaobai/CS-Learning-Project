def trace(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped


@trace
def hi(x):
    return 10


hi(100)
