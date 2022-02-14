# More techniques of 'memoization' (caching)
# x is a hash table where the coordinates are hashed so that calculations
# don't have to be repeated

import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)

x = {}
# calls = {}


def lattice(m, n):
    if m == 1:
        return n + 1
    if n == 1:
        return m + 1
    # print(m, n)
    # Slow:
    # return lattice(m - 1, n) + lattice(m, n - 1)

    # Fast
    if (m, n) in x:
        return x[(m, n)]
    # Since a 19x2 will have the same value as 2x19, we can take advantage of this:
    if (n, m) in x:
        return x[(n, m)]
    x[(m, n)] = lattice(m - 1, n) + lattice(m, n - 1)
    return x[(m, n)]


print(lattice(1000, 1000))
# print(x)
