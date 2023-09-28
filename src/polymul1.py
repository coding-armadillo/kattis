from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = [int(d) for d in input().split()]
    m = int(input())
    b = [int(d) for d in input().split()]
    p = Counter()
    for i in range(n + 1):
        for j in range(m + 1):
            p[i + j] += a[i] * b[j]
    keys = max([k for k in p.keys() if p[k] != 0])
    print(keys)
    print(" ".join([str(p[k]) for k in range(keys + 1)]))
