n = int(input())
e = set()
res = []
for v in input().split():
    v = int(v)
    if v not in e:
        res.append(1)
        e.add(v)
    else:
        res.append(0)
print(*res)
