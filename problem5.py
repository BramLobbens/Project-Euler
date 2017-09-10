# Project Euler - Problem #5

def smallest_multiple(alist):
    '''Return smallest number evenly divisible by
    all numbers in alist'''
    
    n = alist[-1] # should at least be equal to last number in list
    # (or use 2520)

    while True:
        for e in alist:
            if n % e != 0:
                break
        else: # no break
            return n
        n += alist[-1] # increment by largest number in list
        # (or use 2520)

mylist = [e for e in range(1, 21)]
print(smallest_multiple(mylist)) 

# [1..10] => expected answer: 2520
# [1..20] => solution: 232792560