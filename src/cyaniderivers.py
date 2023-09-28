import math

s = input()
t = s.split("1")
print(max([math.ceil(len(z) / 2) for z in t]))
