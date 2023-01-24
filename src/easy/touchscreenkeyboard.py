k = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
]


def d(a, b):
    for r1 in range(3):
        if a in k[r1]:
            c1 = k[r1].index(a)
            break
    for r2 in range(3):
        if b in k[r2]:
            c2 = k[r2].index(b)
            break

    return abs(c1 - c2) + abs(r1 - r2)


for _ in range(int(input())):
    x, n = input().split()
    n, w = int(n), []

    for _ in range(n):
        y = input()
        dist = sum([d(a, b) for a, b in zip(list(x), list(y))])
        w.append([y, dist])

    print("\n".join([f"{k} {v}" for k, v in sorted(w, key=lambda k: (k[1], k[0]))]))
