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

print(sumD(220))

amic = {220, 284}
for i in range(1, 10000):
    if i not in amic:
        x = sumD(i)
        if sumD(x) == i and i != x:
            amic |= {x, i}

print(amic)
print(sum(amic))
