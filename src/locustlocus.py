from math import gcd

n = int(input())
l = []
for _ in range(n):
    y, c1, c2 = [int(d) for d in input().split()]
    g = gcd(c1, c2)
    l.append(y + g * (c1 // g) * (c2 // g))
print(min(l))
