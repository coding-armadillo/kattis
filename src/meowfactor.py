from collections import Counter
from math import ceil, sqrt

c = Counter({1: 9})
n = int(input())
for i in range(2, ceil(sqrt(n))):
    while n % i == 0:
        c[i] += 1
        n //= i
    if i**9 >= n:
        break

t = 1
for k, v in c.items():
    if v >= 9:
        t *= k ** (v // 9)
print(t)
