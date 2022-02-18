from string import ascii_uppercase
with open("p022_names.txt") as f:
    s = f.readline().replace("\"", "").split(",")

print(s)

s.sort()
print(s)

letters = list(ascii_uppercase)
print(letters)
sum_scores = 0
for p, i in enumerate(s):
    score = sum([letters.index(x)+1 for x in i]) * (p + 1)
    sum_scores += score
    if i == 'COLIN':
        print(score)
print(sum_scores)

