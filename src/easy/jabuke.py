xa, ya = [int(d) for d in input().split()]
xb, yb = [int(d) for d in input().split()]
xc, yc = [int(d) for d in input().split()]
n = int(input())
area = abs(xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb)) / 2
print(f"{area:.1f}")


def sign(x1, y1, x2, y2, x3, y3):
    return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)


def in_triangle(x, y, x1, y1, x2, y2, x3, y3):
    d1 = sign(x, y, x1, y1, x2, y2)
    d2 = sign(x, y, x2, y2, x3, y3)
    d3 = sign(x, y, x3, y3, x1, y1)

    has_neg = d1 < 0 or d2 < 0 or d3 < 0
    has_pos = d1 > 0 or d2 > 0 or d3 > 0

    return not (has_neg and has_pos)


total = 0
for _ in range(n):
    x, y = [int(d) for d in input().split()]
    if in_triangle(x, y, xa, ya, xb, yb, xc, yc):
        total += 1
print(total)
