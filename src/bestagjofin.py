n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    v = int(v)
    d[k] = v
print(max(d, key=lambda k: d[k]))
