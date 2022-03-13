def count_while(s, value):
    """Count the number of times that value occurs
    in sequence s.
    
    >>> count_while([1, 2, 1, 2, 1], 1)
    3
    """
    total, index = 0, 0
    while index < len(s):
        element = s[index]
        if element == value:
            total += 1
        index += 1
    return total

def count_for(s, value):
    """Count the number of times that value occurs
    in sequence s.
    
    >>> count_for([1, 2, 1, 2, 1], 1)
    3
    """
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

pairs  = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0

for x, y in pairs:
    if x == y:
        same_count = same_count + 1

same_count
