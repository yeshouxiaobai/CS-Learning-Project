range(5, 8)

range(4)

list(range(4))

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print('Go Bears!')

odds = [1, 3, 5, 7, 9]

[x + 1 for x in odds]

[x for x in odds if 25 % x == 0]

[x+1 for x in odds if 25 % x == 0]

def divisors(n):
    return [1] + [x for x in range(2, n) if n%x == 0]
