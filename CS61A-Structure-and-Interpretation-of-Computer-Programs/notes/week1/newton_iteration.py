def improve(update, good_enough, guess):
    while not good_enough(guess, update(guess)):
        guess = update(guess)
    return guess


def get_newton_update(f, df):
    return lambda x: x - f(x)/df(x)


def sqrt(a):
    def f(x): return x*x - a
    def df(x): return 2*x
    def near_zero(x): return asb(x) < 1e-9
    def good_enough(guess, new_guess):
        return near_zero((guess-new_guess)/guess)

    update = get_newton_update(f, df)
    return improve(update, good_enough, 1.0)


print(sqrt(0.0000000003))
print(sqrt(1000000000000000000000000000000000000000000000))
