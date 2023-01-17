n = int(input())
p = [int(d) for d in input().split()]
prev = []
t = 0
for v in p:
    if not prev:
        prev.append(v)
        continue
    d = (19 + sum(prev)) // len(prev)
    if v <= d:
        prev.append(v)
    else:
        prev = [v]
        t += 1
if prev:
    t += 1
print(t)
