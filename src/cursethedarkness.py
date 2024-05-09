m = int(input())
for _ in range(m):
    bx, by = [float(d) for d in input().split()]
    n = int(input())
    f = False
    for _ in range(n):
        cx, cy = [float(d) for d in input().split()]
        if (bx - cx) ** 2 + (by - cy) ** 2 <= 64:
            f = True
    print("light a candle" if f else "curse the darkness")
