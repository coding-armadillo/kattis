from collections import Counter

n = int(input())
c = Counter()
for _ in range(n):
    t, d, v = input().split()
    v = int(v)
    if d == "IN":
        c[t] += v
    else:
        c[t] -= v
s = sum(c.values())
print(s if s else "NO STRAGGLERS")
