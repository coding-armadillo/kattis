import math


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


coords = {}
for i in range(3):
    n = [int(d) for d in input().split()]
    for j in range(3):
        coords[n[j]] = (i, j)

values = [coords[k] for k in sorted(coords)]
total, prev = 0, 0
for i in range(1, 9):
    total += dist(values[i], values[prev])
    prev = i
print(total)
