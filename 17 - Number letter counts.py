from string import ascii_lowercase
from math import log10

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

p = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion",
     "octillion","nonillion", "decillion", "undecillion","duodecillion", "tredecillion", "quattuordecillion",
     "quindecillion", "sexdecillion", "septendecillion", "octodecillion", "novemdecillion", "vigintillion",
     "unvigintillion", "duovigintillion"]
t = "ten"
h = " hundred"
th = " thousand"


def ntw(n):
    """ ntw = num_to_words """
    if n < 20:
        return ones[n]
    if n < 100:
        if n % 10:
            return tens[n // 10] + "-" + ntw(n % 10)
        return tens[n // 10]
    if n < 1000:
        if n % 100:
            return ntw(n // 100) + h + " and " + ntw(n % 100)
        return ntw(n // 100) + h
    x = (len(str(n)) - 1) // 3
    # x = int(log10(n) / 3)
    w = 10**(3 * x)
    if n % w:
        return ntw(n // w) + ' ' + p[x - 1] + ", " + ntw(n % w)
    return ntw(n // w) + ' ' + p[x - 1]


def lis(s):
    """ lis = letters_in_string """
    return len([i for i in s if i in ascii_lowercase])

# # Answer to problem:
# total = 0
# for i in range(1, 1001):
#     total += lis(ntw(i))
#     if not (i - 1) % 10:
#         print()
#     print(ntw(i))
# print(total)
print(ntw(439805184297052098129387167109285378901424383241239847109238471230478905))
print(ntw(999999999999999999999999999999999999999999999999999999999999999999999999))
# print(lis(ntw(115)))
