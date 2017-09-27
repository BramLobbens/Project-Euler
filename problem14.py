# Project Euler - Problem #14

def generate_chain(n, chain):
    if n == 1:
        return chain
    elif n % 2 == 0:
        n //= 2
        chain.append(n)
        return generate_chain(n, chain)
    else:
        n = (3*n) + 1
        chain.append(n)
        return generate_chain(n, chain)

def print_chain(n):
    mylist = [n]
    my_chain = generate_chain(n, mylist)
    return len(my_chain), my_chain

longest, result = 0, 0
for i in range(1, 1000000):
    length, number = print_chain(i)
    if length > longest:
        longest = length
        result = number[0]

print(longest, result)
