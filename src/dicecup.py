d1, d2 = [int(d) for d in input().split()]

sums = []
for i in range(1, d1 + 1):
    for j in range(1, d2 + 1):
        sums.append(i + j)

from collections import Counter

c = Counter(sums)
most_likely = max(c.values())
for key in sorted(c.keys()):
    if c[key] == most_likely:
        print(key)
