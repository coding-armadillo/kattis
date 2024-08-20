n, m, k = [int(d) for d in input().split()]
b = []
for _ in range(n):
    b.append(list("." * m))
for _ in range(k):
    i, j = [int(d) - 1 for d in input().split()]
    b[i][j] = "*"
print("\n".join("".join(r) for r in b))
