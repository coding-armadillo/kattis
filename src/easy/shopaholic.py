n = int(input())
c = [int(d) for d in input().split()]

c = sorted(c, reverse=True)
groups = [c[i : i + 3] if i + 3 < n else c[i:] for i in range(0, n, 3)]

print(sum(g[-1] if len(g) == 3 else 0 for g in groups))
