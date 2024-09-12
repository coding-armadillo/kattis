n = int(input())
a = [int(d) for d in input().split()]
d = dict(zip(sorted(a), range(n)))
print(*[d[v] for v in a])
