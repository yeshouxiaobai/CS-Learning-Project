# Objects
from datetime import date


date
today = date(2015, 2, 20)
freedom = date(2015, 5, 12)
str(freedom - today)
today.year
today.month
today.day
today.strftime('%A %B %d')

# strings
s = 'Hello'
s.upper()
s.lower()
s.swapcase()
s
a = 'A'
ord(a)
hex(ord(a))

from unicodedata import name, lookup
name('A')
name('a')
lookup('WHITE SMILING FACE')
lookup('SNOWMAN')
lookup('SOCCER BALL')
lookup('BABY').encode()
'A'.encode()

# Mutation Operations
suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()
suits.remove('string')
suits
suits.append('cup')
suits.extend(['sword', 'club'])
suits
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']
suits
original_suits

numerals = {'I': 1, 'V': 5, 'X': 10}
numerals
numerals['X']
numerals['X'] = 11
numerals['X']
numerals
numerals['L'] = 50
numerals
numerals['L']
numerals.pop('X')
numerals.get('X')
numerals

# lists are mutable
def mystery(s):
    s.pop()
    s.pop()

def another_mystery():
    four.pop()
    four.pop()

four = [1, 2, 3, 4]
len(four)
mystery(four)
len(four)
another_mystery()
len(four)

# Tuples: immutable values
(3, 4, 5, 6)
()
tuple()
type([3, 4, 5])
(1,)
2,
(3, 4) + (5, 6)
5 in (3, 4, 5)
# Immutable values are protected from mutation

# Mutation
# Identity Operators
# <exp0> is <exp1>
# Equality
# <exp0> == <exp1>
[10] == [10]
a = [10]
b = [10]
a == b
a is b
a.extend([20, 30])
a
b
c = b
c is b
c.pop()
c
a

# Mutable Default Arguments are Dangerous
def f(s=[]):
    s.append(5)
    return len(s)
f()
f()
f()
