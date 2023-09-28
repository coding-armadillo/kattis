while True:
    line = input()
    if line == "0":
        break
    x1, y1, x2, y2, p = [float(d) for d in line.split()]
    print((abs(x1 - x2) ** p + abs(y1 - y2) ** p) ** (1 / p))
