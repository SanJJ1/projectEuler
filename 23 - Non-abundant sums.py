def sumD(n):
    i = 2
    s = {1}
    while i * i <= n:
        if not n % i:
            s |= {i, n // i}
            s.add(i)
            s.add(n // i)
        i += 1
    # print(s)
    return sum(s)


print(sumD(0))
l = [i for i in range(1, 28125) if sumD(i) > i]

print(l)

combos = {24}

for i in l:
    for j in l:
        combos.add(i + j)

combosSum = sum(combos)
print(combos)

nonSum = 0
for i in range(28123 + 1):
    if i not in combos:
        nonSum += i
print(nonSum)
