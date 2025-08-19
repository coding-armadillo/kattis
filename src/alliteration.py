from collections import Counter

n = int(input())
for _ in range(n):
    d = Counter(c[0] for c in input().split())
    print(max(d, key=lambda v: (d[v], -ord(v))))
