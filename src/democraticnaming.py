from collections import Counter

n, m = [int(d) for d in input().split()]
names = []
for _ in range(n):
    names.append(input())

name = ""
for j in range(m):
    c = Counter(names[i][j] for i in range(n))
    name += max(c, key=lambda k: (c[k], -ord(k)))
print(name)
