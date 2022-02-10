x = 1
y = 2

s = 0
while y < 4e6:
    temp = x
    x = y
    # print(y)
    if not y % 2:
        s += y
        print(y)
    y = temp + x

print(s)