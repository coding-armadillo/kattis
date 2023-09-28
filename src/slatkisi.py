c, k = [int(d) for d in input().split()]
d = 10**k
c = (c // d) * d + (d if (c % d) / d >= 0.5 else 0)
print(c)
