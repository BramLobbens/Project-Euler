# Project Euler - Problem #3

from math import sqrt

test_value = 9

def is_prime(n):
    '''Return True if n, int is prime. False otherwise'''
    if (n > 2 and n % 2 == 0) or (n == 1):
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def largest_prime_fac(n):
    '''Return the largest prime factor, given n, int'''
    factor = 0
    for i in range(3, int(sqrt(n)) + 1, 2):
        factor = n / i
        if is_prime(factor):
            return factor
    return None
    
print(largest_prime_fac(test_value))