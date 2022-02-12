l = {1: 1}


# # Inefficient but informative way:
# l[1] = [1, [1]]
# def chainl(n): # inefficient but keeps track of sequences
#     if n in l.keys():
#         return l[n]
#     elif n & 1:
#         x = chainl(3 * n + 1)
#         l[n] = [x[0] + 1, [n] + x[1]]
#     else:
#         x = chainl(n // 2)
#         l[n] = [x[0] + 1, [n] + x[1]]
#     return l[n]

# max = 0
# for i in range(1, 1000000):
#     chainl(i)
#     x, y = l[i]
#     if x > max:
#         max = x
#         print(f"{i} : {max}")
# print(i, ":", x)
# y = " -> ".join([str(i) for i in y])
# print(f"{i} : {x} : {y}")


# Efficient way:


def chainl(n):
    if n in l:
        return l[n]
    elif n & 1:
        l[n] = chainl(3 * n + 1) + 1
    else:
        l[n] = chainl(n >> 1) + 1
    return l[n]


m = 0
for i in range(1, int(1e6)):
    x = chainl(i)
    if x > m:
        m = x
        print(f"{i} : {m}")
    # print(i, ":", x)
