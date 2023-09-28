import math

n, x, y = [int(d) for d in input().split()]
i = [int(input()) for _ in range(n)]

# for python 3.9+ (https://docs.python.org/3.9/library/math.html#math.gcd)
# s = math.gcd(x, *i)

s = math.gcd(x, i[0])
for k in range(1, n):
    s = math.gcd(s, i[k])

x /= s
i = [v / s for v in i]

scale = y / x
for v in i:
    print(int(scale * v))
