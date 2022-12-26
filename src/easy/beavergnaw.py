import math

while True:
    D, V = [int(d) for d in input().split()]
    if not D and not V:
        break
    # R = D / 2
    # r = d / 2
    # V + π * (r**2) * (2*r) + 2 * (1/3) * π * (R-r) * (r**2 + r*R + R**2) == π * (R**2) * (2*R)
    print(math.pow(D**3 - 6 * V / math.pi, 1 / 3))
