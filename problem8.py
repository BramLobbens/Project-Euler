# Project Euler - Problem #8

from functools import reduce

with open('problem8_number.txt', 'r') as read_file:
    content = read_file.read()
number = content.replace('\n', '') # type str

f = lambda x, y: int(x) * int(y)
greatest_product = 0

for i in range(len(number)-13):
    product = reduce(f, number[i:i+13])
    if product > greatest_product:
        greatest_product = product

print(greatest_product)
read_file.close()