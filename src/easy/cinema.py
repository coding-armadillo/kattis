n,m = [int(v) for v in input().split()]
#n = total copacity of cinema
#m is number of groups

size = [int(v) for v in input().split()]

groups_admitted = 0

for i in range(m):
    if size[i] <= n:
        n -= size[i]
        groups_admitted += 1

print(m - groups_admitted)
    
