n = int(input())
a = [int(d) for d in input().split()]
t = 0
while True:
    p = a.index(min(a)) + 1
    t += min(a[: p + 1]) * p
    a = a[p:]
    if not a:
        break
print(t)
