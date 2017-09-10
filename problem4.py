# Project Euler - Problem #4
# Largest palindrome product

biggest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        string = str(i * j)
        if string[0] == string[-1]:
            if string[1] == string[-2]:
                if string[2] == string[-3]:
                    pal = int(string)
                    if pal > biggest:
                        biggest = pal

print(biggest)