from operator import add


def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


m = curry2(add)
add_three = m(3)
add_three(2)
add_three(2010)


def curry2(f): return lambda x: lambda y: f(x, y)


m = curry2(add)
m(2)(3)
