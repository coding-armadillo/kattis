n = int(input())
d = {}
for _ in range(n):
    s, v = input().split()
    v = int(v)
    if s not in d:
        d[s] = v
    else:
        d[s] += v
print(max(d, key=lambda k: d[k]))
