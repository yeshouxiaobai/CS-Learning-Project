numerals = {'I': 1, 'V': 5, 'X': 10}

numerals['X']

numerals.keys()

numerals.values()

numerals.items()

item = [('I', 1), ('V', 5), ('X', 10)]

dict(item)

'X' in numerals

numerals.get('X', 0)

numerals.get('X-ray', 0)

squares = {x: x*x for x in range(10)}

squares[7]

{1: 2, 1: 3}  # Only get one item.
