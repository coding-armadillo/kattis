import math

t = int(input())
for _ in range(t):
    n = int(input())
    print((math.floor(math.sqrt(n + 1)) - 1) // 2)
