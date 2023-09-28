x1, y1 = [int(d) for d in input().split()]
x2, y2 = [int(d) for d in input().split()]
x3, y3 = [int(d) for d in input().split()]

d12 = (x1 - x2) ** 2 + (y1 - y2) ** 2
d13 = (x1 - x3) ** 2 + (y1 - y3) ** 2
d23 = (x2 - x3) ** 2 + (y2 - y3) ** 2

if d12 == d13:
    x, y = x2 + x3 - x1, y2 + y3 - y1
elif d12 == d23:
    x, y = x1 + x3 - x2, y1 + y3 - y2
else:
    x, y = x1 + x2 - x3, y1 + y2 - y3

print(x, y)
