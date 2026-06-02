from math import ceil

l, w, v = [int(d) for d in input().split()]
print((ceil(l * w / v) - 1) * 4 + 3)
