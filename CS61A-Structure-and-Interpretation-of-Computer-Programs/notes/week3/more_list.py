# assume that before each example blow we execute:
s = [2, 3]
t = [5, 6]

# append adds one
s.append(t)

# extend adds all
s.extend(t)

# addition and slicing
a = s + [t]
b = a[1:]
a[1] = 9
b[1][1] = 0

# The List function
t = list(s)
s[1] = 0

# slice assignment
s[0:0] = t
s[3:] = t
t[1] = 0

# pop
t = s.pop()

# remove
t.extend(t)
t.remove(5)

# slice assignment
s[:1] = []
t[0:2] = []

# examples
t = [1, 2, 3]
t[1:3] = [t]
t.extend(t)

t = [[1, 2], [3, 4]]
t[0].append(t[1:2])
