n = int(input())
c = [int(input()) for _ in range(n)]

c = sorted(c, reverse=True)
groups = [c[i : i + 3] if i + 3 < n else c[i:] for i in range(0, n, 3)]

print(sum(sum(g if len(g) < 3 else g[:2]) for g in groups))
