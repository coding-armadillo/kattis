from collections import Counter

n, k = [int(d) for d in input().split()]
c = Counter()
for _ in range(n):
    a, b = [int(d) for d in input().split()]
    c.update(range(a, b))
print(len([_ for _, v in c.items() if v >= k]))
