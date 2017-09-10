# Project Euler - Problem #2
# Even Fibonacci numbers

TEST_CASE = 4000000

def fibonacci(n):
    '''Return fibonacci number of n, int'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fib_even(n):
    '''
    Return sum of sequence of even fibonacci
    numbers up to limit n, int
    '''
    num = 0
    even_fibs = []
    fib_seq = fibonacci(num)
    
    while fib_seq < n:
        if (fib_seq % 2) == 0:
            even_fibs.append(fib_seq)
        fib_seq = fibonacci(num)
        num += 1
    return sum(even_fibs)
    
print(fib_even(TEST_CASE))