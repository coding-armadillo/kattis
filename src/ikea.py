import math

k = int(input())
n = int(input())
a, b = n // k, math.ceil(n / k)

items = []
for _ in range(n):
    s = input().split()
    items.append((s[0], int(s[1])))
items = sorted(items, key=lambda v: v[1])

sum0, sum1, sum2 = (
    sum([t[1] for t in items[:a]]),
    sum([t[1] for t in items[:b]]),
    sum([t[1] for t in items[b : b + a]]),
)

if sum1 < sum2:
    print(sum1)
    print(*sorted([t[0] for t in items[:b]]), sep="\n")
else:
    print(sum0)
    print(*sorted([t[0] for t in items[:a]]), sep="\n")
