l = {i * i for i in range(1, 700)}

special = []
for a in range(1, 1000):
    for b in range(a + 1, 1000):
        if a ** 2 + b ** 2 in l:
            c = int((a ** 2 + b ** 2) ** .5)
            print(a, b, int((a ** 2 + b ** 2) ** .5))
            if a + b + c == 1000:
                special = [a, b, c]

print(special)
from math import prod
print(prod(special))