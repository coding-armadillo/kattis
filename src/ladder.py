import math

h, v = [int(d) for d in input().split()]
print(math.ceil(h / math.sin(math.radians(v))))
