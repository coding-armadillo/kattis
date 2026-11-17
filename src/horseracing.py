n, d = [int(_) for _ in input().split()]
hs = []
for _ in range(n):
    sp, st = [int(_) for _ in input().split()]
    if st >= d:
        t = d / sp
    else:
        t = st / sp + (d - st) / sp * 2
    hs.append(t)
print(hs.index(min(hs)))
