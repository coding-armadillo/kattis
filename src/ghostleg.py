n, m = [int(d) for d in input().split()]
v = [str(d) for d in list(range(1, n + 1))]
for _ in range(m):
    a = int(input())
    v[a - 1], v[a] = v[a], v[a - 1]
print("\n".join(v))
