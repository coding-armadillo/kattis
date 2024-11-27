from collections import Counter

n = int(input())
c = Counter()
for i in range(2 * n):
    name = input()
    if i % 2:
        c[name] += 1
for k, v in c.items():
    print(k, v)
