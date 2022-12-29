import math

for _ in range(int(input())):
    v0, a, x1, h1, h2 = [float(d) for d in input().split()]
    a = math.radians(a)
    t = x1 / (v0 * math.cos(a))
    y = v0 * t * math.sin(a) - 0.5 * 9.81 * (t**2)
    if y < h1 + 1 or y > h2 - 1:
        print("Not Safe")
    else:
        print("Safe")
