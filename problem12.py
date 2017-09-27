# Project Euler - Problem #12

import math
from time import time

# Helper function
def generate_triangle_number(n):
    '''Assume n is a positive int.
    Return the triangle number of n terms.'''
    result = 0
    for i in range(n+1):
        result += i
    yield result

# Helper function
def num_divs(n):
    '''Return number of divisors of int n'''
    divs = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
           divs += 1
           if i*i != n:
               divs += 1
    return divs

def get_triangle_number(n):
    '''Assume n is a positive int.
    Return triangle number with n number of divisors.'''
    m = 1
    while True:
        for number in generate_triangle_number(m):
            divs = num_divs(number)
            if divs >= n:
                return number#, m, divs
        m += 1

t1 = time()
print(get_triangle_number(500))
t2 = t1 - time()
print(t2)
