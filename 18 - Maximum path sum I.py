s = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


l = [[int(j) for j in i.split()] for i in s.split("\n")]
print(l)
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def maxpath(self):
        if self.left and self.right:
            return max(self.left.maxpath(), self.right.maxpath()) + self.value
        return self.value

    def __str__(self):
        if self.left and self.right:
            return f"|{self.value}, {self.left.value}, {self.right.value}|"
        return f"|{self.value}, None, None|"

    def __repr__(self):
        return self.__str__()

# print(sum([len(i) for i in l]))
x = [[] for i in range(len(l))]

for i in range(len(l)):
    for j in range(i + 1):
        x[i].append(Node(l[i][j]))
print(x)

for i in range(len(l) - 1):
    for j in range(i + 1):
        x[i][j].left = x[i + 1][j]
        x[i][j].right = x[i + 1][j + 1]

print(x)

print(x[0][0].maxpath())

