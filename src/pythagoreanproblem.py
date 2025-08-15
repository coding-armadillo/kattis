import math

a, b = [int(d) for d in input().split()]
c1 = math.sqrt(a**2 + b**2)
c2 = math.sqrt(abs(a**2 - b**2))
v = [int(c) for c in [c1, c2] if c.is_integer() and c]
print("Pythagoras is sad :(" if not v else min(v))
