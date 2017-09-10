# Project Euler - Problem #10

from time import time
def sum_primes(number):
    '''Generate prime numbers'''
    
    primes = [] # store primes
    n = 2
    
    while True:
        for p in primes:
            if n % p == 0:
                break
        else: # no break
            if n >= number:
                return sum(primes)
            primes.append(n)
        n += 1

t1 = time()        
print(sum_primes(2000000)) # => warning: takes 40mins
t2 = time() - t1
print(t2)