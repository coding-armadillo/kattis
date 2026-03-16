from collections import Counter

n = int(input())
p = [input().split() for _ in range(n)]
c = Counter()
for a, b in p:
    b = float(b[1:])
    c[a] += b
    print(f"{a} ${c[a]:.2f}")
