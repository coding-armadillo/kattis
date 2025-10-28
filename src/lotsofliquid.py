import math

input()
c = [float(n) for n in input().split()]
print(math.pow(sum(n**3 for n in c), 1 / 3))
