from collections import Counter

d = Counter()
for _ in range(int(input())):
    d[input()] = 0

for _ in range(int(input())):
    l = input().split()
    if len(l) == 1:
        continue
    for n in l[1:]:
        d[n] += 1

for k in sorted(d, key=lambda k: -d[k]):
    print(d[k], k)
