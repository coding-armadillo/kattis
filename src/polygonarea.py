while True:
    n = int(input())
    if not n:
        break
    p = [[int(d) for d in input().split()] for _ in range(n)]
    a, b = 0, 0
    for i in range(n - 1):
        a += (p[i + 1][0] - p[i][0]) * (p[i + 1][1] + p[i][1])
        b += p[i][0] * p[i + 1][1] - p[i][1] * p[i + 1][0]

    a += (p[0][0] - p[-1][0]) * (p[0][1] + p[-1][1])
    b += p[-1][0] * p[0][1] - p[-1][1] * p[0][0]

    print("CCW" if a < 0 else "CW", f"{abs(b/2):.1f}")
