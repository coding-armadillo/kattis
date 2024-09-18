from itertools import product

n = int(input())

l = []
for _ in range(n):
    l.append(sorted(input().split()[1:]))

for row in product(*l):
    print(" ".join(row))
