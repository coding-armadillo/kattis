n, m = [int(d) for d in input().split()]
p = [0] * n
for _ in range(m):
    a, b = [int(d) - 1 for d in input().split()]
    p[a] += 1
    p[b] += 1
print(" ".join([str(a - b) for a, b in zip(p, range(1, 1 + n))]))
