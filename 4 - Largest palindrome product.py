pals = []


def is_pal(n):
    return str(n) == str(n)[::-1]


for i in range(100, 1000):
    for j in range(100, 1000):
        if is_pal(i * j):
            pals.append(i * j)
            if i *j == 906609:
                print(i, j)

pals.sort(reverse=True)
print(pals)
