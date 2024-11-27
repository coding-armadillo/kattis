from collections import Counter

n = int(input())
m = int(input())
g = dict(zip(range(n), input().split()))

c = Counter()
for _ in range(m):
    v = [int(d) for d in input().split()]
    for i in range(n):
        c[g[i]] += v[i]
print(max(c, key=lambda v: c[v]))
