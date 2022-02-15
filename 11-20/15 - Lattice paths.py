# More techniques of 'memoization' (caching)
# x is a hash table where the coordinates are hashed so that calculations
# don't have to be repeated

import sys

# print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)

x = {}
# calls = {}


def lat(m, n):
    if m == 0:
        return 1
    if n == 0:
        return 1
    # print(m, n)
    # Slow:
    # return lattice(m - 1, n) + lattice(m, n - 1)

    # Fast
    if (m, n) in x:
        return x[(m, n)]
    # Since a 19x2 will have the same value as 2x19, we can take advantage of this:
    if (n, m) in x:
        return x[(n, m)]
    x[(m, n)] = lat(m - 1, n) + lat(m, n - 1)
    return x[(m, n)]


print(lat(1200, 1100))
# # # Prints Pascal's triangle using the lattice method
# # [print(" ".join([str(lat(i - j, j)) for j in range(i + 1)])) for i in range(10)]
# for i in range(41):
#     for j in range(i + 1):
#         print(lat(i - j, j), end =" ")
#     print()
