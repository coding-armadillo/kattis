for _ in range(int(input())):
    values = [int(d) for d in input().split()]
    coords = values[1:]
    n = values[0]

    coords.append(coords[0])
    coords.append(coords[1])

    area = 0
    for i in range(0, 2 * n, 2):
        x1, y1 = coords[i], coords[i + 1]
        x2, y2 = coords[i + 2], coords[i + 3]
        area += x1 * y2 - x2 * y1

    print(0.5 * abs(area))
