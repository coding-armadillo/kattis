import math

n, d = [int(d) for d in input().split()]
v = [int(d) for d in input().split()]
lcm = n * d // math.gcd(n, d)
print(sum(v[i % n] for i in range(0, lcm, d)))
