from collections import Counter

n, c = [int(d) for d in input().split()]
m = Counter()
for _ in range(n):
    t, p = [int(d) for d in input().split()]
    m[t] = min(m[t], p) if t in m else p
ans = 0
m = sorted(m.items(), key=lambda t: t[1])
for k in m:
    if c - k[1] >= 0:
        ans += 1
        c -= k[1]
    else:
        break
print(ans)
