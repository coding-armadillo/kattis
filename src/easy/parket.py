import math

r, b = [int(d) for d in input().split()]
w = math.floor((r + b) ** 0.5)
while w:
    if (r + b) / w == (r + 4) / 2 - w:
        print((r + 4) // 2 - w, w)
        break
    w -= 1
