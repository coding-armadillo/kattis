import math

m, n, r = input().split()
m = int(m)
n = int(n)
r = float(r)
coords = [int(d) for d in input().split()]
p = r / n

dist1 = 0
dist1 += p * abs(coords[1] - coords[3])
dist1 += (
    math.pi
    * r
    * ((min(coords[3], coords[1]) if coords[3] != coords[1] else coords[1]) / n)
    * (abs(coords[0] - coords[2]) / m)
)

dist2 = p * abs(coords[1] + coords[3])

print(min(dist1, dist2))
