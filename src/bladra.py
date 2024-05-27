from collections import Counter

k, q = [int(d) for d in input().split()]
m = Counter()
for _ in range(q):
    a, b = [int(d) for d in input().split()]
    m[b] += 1
print(0 if len(m.keys()) < k else min(m.values()))
