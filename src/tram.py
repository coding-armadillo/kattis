n = int(input())
d = 0
for _ in range(n):
    x, y = [int(i) for i in input().split()]
    d += 2 * (x - y)
print(-d / (2 * n))
