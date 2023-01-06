from collections import Counter

lc = 0
while True:
    n = int(input())
    if not n:
        break
    lc += 1
    l = Counter()
    for _ in range(n):
        animal = input().lower().split()
        l[animal[-1]] += 1
    print(f"List {lc}:")
    print("\n".join([f"{k} | {l[k]}" for k in sorted(l)]))
