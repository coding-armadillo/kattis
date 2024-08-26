n = int(input())
a = [int(d) for d in input().split()]
m = dict(zip(range(1, n + 1), a))
print(*sorted(m, key=lambda v: -m[v]))
