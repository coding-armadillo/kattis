n = int(input())
l = []
s = 0
for _ in range(n):
    a, b = [int(d) for d in input().split()]
    if a > b:
        s += 1
    else:
        l.append(s)
        s = 0
print(s if not l else max(s, max(l)))
