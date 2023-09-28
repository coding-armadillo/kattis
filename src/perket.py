from itertools import combinations

n = int(input())
l = [[int(d) for d in input().split()] for _ in range(n)]

c = []
for i in range(1, n + 1):
    c.extend(list(combinations(l, i)))

d = []
for i in c:
    s, b = 1, 0
    for x, y in i:
        s *= x
        b += y
    d.append(abs(s - b))

print(min(d))
