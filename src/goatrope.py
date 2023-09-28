x, y, x1, y1, x2, y2 = [int(d) for d in input().split()]

if x >= x1 and x <= x2:
    print(min(abs(y - y1), abs(y - y2)))
elif y >= y1 and y <= y2:
    print(min(abs(x - x1), abs(x - x2)))
else:
    x3, y3 = x1, y2
    x4, y4 = x2, y1
    l = [
        ((x - a) ** 2 + (y - b) ** 2) ** 0.5
        for a, b in [(x1, y1), (x2, y2), (x1, y2), (x2, y1)]
    ]
    print(min(l))
