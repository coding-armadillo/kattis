from collections import Counter

n = int(input())
for i in range(n):
    _ = input()
    c = Counter(input().split())
    print(f"Case #{i+1}: {' '.join(v for v in c if c[v]==1)}")
