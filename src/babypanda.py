import math

n, m = [int(d) for d in input().split()]
d = 0
while m:
    c = math.floor(math.log(m, 2))
    d += 1
    m -= 2**c
print(d)
