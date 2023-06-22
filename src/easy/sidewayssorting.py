while True:
    r, c = [int(d) for d in input().split()]
    if not r and not c:
        break
    s = []
    for _ in range(r):
        s.append(input())
    items = []
    for i in range(c):
        items.append("".join(s[j][i] for j in range(r)))
    items = sorted(items, key=lambda t: t.lower())
    for i in range(r):
        print("".join(items[j][i] for j in range(c)))
