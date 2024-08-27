def dist2(b1, b2):
    return (b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2


while True:
    d, n = input().split()
    d = float(d)
    n = int(n)
    if not d and not n:
        break
    b = []
    for _ in range(n):
        x, y = [float(v) for v in input().split()]
        b.append((x, y))
    b = sorted(b, key=lambda v: (v[0], v[1]))

    sour = set()

    for i in range(len(b)):
        if len(sour) == n:
            break
        for j in range(i + 1, len(b)):
            if len(sour) == n:
                break
            if dist2(b[i], b[j]) < d**2:
                sour.add(i)
                sour.add(j)

    nsour = len(sour)
    nsweet = n - nsour
    print(f"{nsour} sour, {nsweet} sweet")
