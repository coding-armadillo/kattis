from collections import Counter

n = int(input())
c = Counter()
for _ in range(n):
    c[input()] += 1
print("\n".join(sorted([k for k, v in c.items() if v == min(c.values())])))
