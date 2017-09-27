# Project Euler - Problem #16

from functools import reduce

f = lambda x, y: x + y
mylist = list(str(2**1000))
result = reduce(f, [int(e) for e in mylist])

print(result)
