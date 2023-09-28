n, m = [int(v) for v in input().split()]

size = [int(v) for v in input().split()]

groups_admitted = 0

for i in range(m):
    if size[i] <= n:
        n -= size[i]
        groups_admitted += 1

print(m - groups_admitted)
