n = int(input())
p = [int(d) for d in input().split()]
nb = 0
for i in range(n - 1):
    if p[i + 1] > p[i]:
        nb += 1
print(nb)
