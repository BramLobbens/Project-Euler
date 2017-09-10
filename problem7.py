# Project Euler - Problem #7

def get_prime(number):
    '''Return nth (number) prime number'''

    primes = [] # store primes
    n = 2

    while True:
        for p in primes:
            if n % p == 0:
                break
        else: # no break
            primes.append(n)
            if len(primes) == number:
                return n
        n += 1

print(get_prime(10001)) # => return 10001th prime number
