def in_rectangle(x1, y1, x2, y2, x, y):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    if x in range(x1, x2 + 1) and y in range(y1, y2 + 1):
        return True
    else:
        return False


def in_circle(x0, y0, r, x, y):
    return (x0 - x) ** 2 + (y0 - y) ** 2 <= r**2


m = int(input())
shapes = []
for _ in range(m):
    values = input().split()
    shapes.append((values[0], *[int(d) for d in values[1:]]))

n = int(input())
for _ in range(n):
    total = 0
    x, y = [int(d) for d in input().split()]
    for shape in shapes:
        if shape[0] == "rectangle":
            total += in_rectangle(*shape[1:], x, y)
        elif shape[0] == "circle":
            total += in_circle(*shape[1:], x, y)
    print(total)
