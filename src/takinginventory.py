from collections import Counter
from math import ceil

n = int(input())
i = Counter()
for _ in range(n):
    s, m = input().split()
    i[s] += int(m)
for s, m in i.items():
    print(s, ceil(m / 64))
