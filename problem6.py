# Project Euler - Problem #6

from functools import reduce
f = lambda x, y: x + y
# 1. get sum of first hundred squares
sum_of_square = reduce(f, [e**2 for e in range(1 ,101)])
# 2. get sum of first hundred numbers -> square
square_of_sum = reduce(f, [e for e in range(1, 101)])**2
# 3. difference between both sums
print(square_of_sum - sum_of_square)
