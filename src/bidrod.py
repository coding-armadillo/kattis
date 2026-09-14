input()
x = [int(d) for d in input().split()]
v = set()
a = []
for d in x:
    if d not in v:
        a.append(d)
        v.add(d)
print(*a)
