n = int(input())
c, m = 0, 0
for _ in range(n):
    a, b = [int(d) for d in input().split()]
    c += b - a
    m = max(m, c)
print(m)
