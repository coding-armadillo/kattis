n = int(input())
p = [int(d) for d in input().split()]
p = sorted(p)
t = 0
for i in range(0, n // 2 + 1):
    t += p[i] // 2
for i in range(n // 2 + 1, n):
    t += p[i]
print(t)
