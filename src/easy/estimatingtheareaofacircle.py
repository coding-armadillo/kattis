import math

while True:
    r, m, c = input().split()
    if r == "0" and m == "0" and c == "0":
        break
    r = float(r)
    m, c = int(m), int(c)
    print(math.pi * r * r, 4 * r * r * c / m)
