n, m = [int(d) for d in input().split()]
p = []
for _ in range(n):
    p.append([int(d) for d in input().split()])

f = False
for i in range(1, n - 1):
    for j in range(1, m - 1):
        c = []
        c.append(p[i - 1][j])
        c.append(p[i][j - 1])
        c.append(p[i + 1][j])
        c.append(p[i][j + 1])
        if all(v > p[i][j] for v in c):
            f = True
            break
    if f:
        break

print("Jebb" if f else "Neibb")
