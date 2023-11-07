x, y = [int(d) for d in input().split()]
if y == 1:
    print("ALL GOOD" if not x else "IMPOSSIBLE")
else:
    print(-x / (y - 1))
