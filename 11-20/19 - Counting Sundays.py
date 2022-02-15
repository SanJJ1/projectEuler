count = 1
d = 1
m = 1
y = 1900

sundaycount = 0
while y < 2000 or m < 12 or d < 31:
    # print(m, d, y)
    count += 1
    d += 1
    if d > 28:
        if m == 2:
            if ((not (y % 400)) or (y % 100 and (not y % 4))) and d < 30:
                pass
            else:
                d = 1
                m += 1
        elif d > 30 and m in [9, 4, 6, 11]:
            d = 1
            m += 1
        elif d > 31:
            d = 1
            m += 1
            if m > 12:
                y += 1
                m = 1
    if not count % 7 and d == 1 and y > 1900:
        sundaycount += 1
        print(m, d, y)

print(m, d, y)

print(sundaycount)