import math

while True:
    r, h, s = [int(d) for d in input().split()]
    if not r and not h and not s:
        break
    l = math.sqrt(h**2 - r**2) * 2
    a = math.pi-math.acos(r / h)
    l += 2 * math.pi * r * (a / math.pi)
    l *= 1 + s / 100
    print(f"{l:.2f}")
