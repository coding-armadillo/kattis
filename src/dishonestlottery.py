from collections import Counter

n = int(input())
x = Counter()
for _ in range(10 * n):
    x.update([int(d) for d in input().split()])
res = [k for k in x if x[k] > 2 * n]
if not res:
    print(-1)
else:
    print(*sorted(res))
