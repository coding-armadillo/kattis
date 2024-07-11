from collections import Counter

n, m = [int(d) for d in input().split()]
t = Counter([int(input()) for _ in range(n)])
print("Ja" if max(t.values()) + m >= n else "Nej")
