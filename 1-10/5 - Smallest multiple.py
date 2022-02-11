from math import prod

l = [1]
for i in range(2, 21):
    j = 1
    while prod(l) * j % i != 0:
        j += 1
    l.append(j)

ans = prod(l)

for i in range(1, 21):
    print(ans / i)
print(l)
