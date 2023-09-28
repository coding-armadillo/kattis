h, k, v, s = [int(d) for d in input().split()]
t = 0
while h > 0:
    v += s
    v -= max(1, v // 10)
    if v >= k:
        h += 1
    elif v > 0:
        h -= 1
        if not h:
            v = 0
    else:
        h = 0
        v = 0
    t += v
    if s > 0:
        s -= 1
print(t)
