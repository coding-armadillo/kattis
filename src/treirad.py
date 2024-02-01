import math

n = int(input())

t = 0
for i in range(1, math.ceil(n ** (1 / 3))):
    if i * (i + 1) * (i + 2) < n:
        t += 1
print(t)
