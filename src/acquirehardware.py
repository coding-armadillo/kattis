h, w = [int(d) for d in input().split()]
m, a = [], []

for _ in range(h):
    m.append(input())
    s = []
    for _ in range(w):
        s.append(0)
    a.append(s)

for i in range(w):
    for j in range(h):
        c = []
        if i - 1 >= 0:
            c.append(a[j][i - 1])
        if j - 1 >= 0:
            c.append(a[j - 1][i])
        if m[j][i] == "I":
            a[j][i] = (max(c) if c else 0) + 1
        else:
            a[j][i] = max(c) if c else 0

print(a[h - 1][w - 1])
