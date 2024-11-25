n, h = int(input()), 0
for _ in range(n):
    t, a = [int(d) for d in input().split()]
    h = max(h - a, 0) if t else h + a
print(h)
