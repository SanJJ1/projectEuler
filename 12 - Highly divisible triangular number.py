

def factrs(n):
    l = [1, n]
    d = 2
    while d * d <= n:
        if not n % d:
            l += [d, n // d]
        d += 1
    return l
    # return sorted(l)

i = 1
l = 1
while l < 500:
    tri = sum(range(1, i + 1))
    fax = factrs(tri)
    # l = len(fax)
    if len(fax) > l:
        l = len(fax)
        print(f"{i} : {tri} : {l} : {fax}")
    i += 1