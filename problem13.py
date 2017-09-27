# Project Euler - Problem #13

with open('problem13_number.txt', 'r') as read_file:
    content = read_file.read()
number = content.split('\n')

result = 0
for num in number:
    result += int(num)

print(str(result)[:10])
