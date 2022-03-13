def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    
    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    return paths(m-1, n) + paths(m, n-1)

def kanp(n, k):
    if n == 0:
        return k == 0
    with_last = knap(n//10, k-n%10)
    without_last = knap(n//10, k)
    return with_last or without_last

def count_partitions(n, m):
    """The number of partitions of a positive integer n,
    using parts up to size m, is the number of ways
    in which n can be expressed as the sum of positive
    interger parts up to m in increasing order.
    
    >>> count_partitions(5, 3)
    5
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m

def all_nums(k):
    def h(k, prefix):
        if k == 0:
            print(prefix)
            return
        h(k-1, prefix*10)
        h(k-1, prefix*10+1)
    h(k, 0)

def remove(n, digit):
    """Return all digits of non-negative N that are not DIGIT,
    for some non-negative DIGIT less than 10.
    
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + last*10**digits
            digits = digits + 1
    return kept
