n, k = [int(d) for d in input().split()]
d = [int(d) for d in input().split()]
s = 0
for i in range(0, n - k + 1):
    v = sum(d[i : i + k])
    if v > s:
        s = v
print(s)
