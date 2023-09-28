import math

a, b, c, d = [int(d) for d in input().split()]
s = (a + b + c + d) / 2
print(math.sqrt((s - a) * (s - b) * (s - c) * (s - d)))
