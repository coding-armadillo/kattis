import math

while True:
    try:
        r, x, y = [float(d) for d in input().split()]
    except:
        break
    if x**2 + y**2 >= r**2:
        print("miss")
    else:
        # https://mathworld.wolfram.com/CircularSegment.html
        d = math.sqrt(x**2 + y**2)
        h = r - d
        a = math.acos((r - h) / r)
        t = (r - h) * math.sqrt(2 * r * h - h * h)
        p = (r**2) * a
        s = p - t
        print(math.pi * (r**2) - s, s)
