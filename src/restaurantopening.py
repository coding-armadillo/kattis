from itertools import product

n, m = [int(d) for d in input().split()]

g = []
for _ in range(n):
    g.append([int(d) for d in input().split()])

l = list(product(range(n), range(m)))

c = []
for i, j in l:
    s = 0
    for a, b in l:
        s += g[a][b] * (abs(i - a) + abs(j - b))
    c.append(s)

print(min(c))
