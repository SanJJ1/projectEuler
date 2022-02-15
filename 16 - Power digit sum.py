# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

def sumdigits(n):
    return sum([int(i) for i in str(n)])

# for i in range(25):
#     print(i,2**i, sumdigits(2**i))

print(sumdigits(2**1000))