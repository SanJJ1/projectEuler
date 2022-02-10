l = []

x = 600851475143
n = 2
while n != x:
    if x % n == 0:
        x = x // n
        l.append(n)
        n = 2
    else:
        n += 1
    # print(x, n)
l.append(n)
l.sort()
print(l[-1])
print(l)
