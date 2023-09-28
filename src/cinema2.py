n, m = [int(t) for t in input().split()]
p = [int(t) for t in input().split()]

d = 0
l = 0
for i in range(m):
    if p[i] > n - d:
        break
    else:
        k = p[i]
        d += k
        l += 1

print(m - l)
