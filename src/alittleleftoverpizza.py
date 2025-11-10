from collections import Counter
from math import ceil

n = int(input())
c = Counter()
for _ in range(n):
    s, l = input().split()
    l = int(l)
    if l:
        c[s] += l
m = {"S": 6, "M": 8, "L": 12}
print(sum((ceil(d / m[s]) for s, d in c.items())))
