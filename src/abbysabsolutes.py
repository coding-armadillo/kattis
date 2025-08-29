n, _ = [int(d) for d in input().split()]
k = [int(d) for d in input().split()]
print(*[1 if abs(d - 1) <= abs(n - d) else n for d in k])
