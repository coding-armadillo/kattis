from collections import Counter

n, m = [int(d) for d in input().split()]
d = [input() for _ in range(n)]
c = Counter()
for _ in range(m):
    name = input()
    print(d[c[name] % n])
    c[name] += 1
