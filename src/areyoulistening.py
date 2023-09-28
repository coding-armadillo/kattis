import math

cx, cy, n = [int(d) for d in input().split()]

d = []
for _ in range(n):
    x, y, r = [int(d) for d in input().split()]
    d.append(((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 - r)
v = sorted(d)[2]
print(math.floor(v) if v > 0 else 0)
