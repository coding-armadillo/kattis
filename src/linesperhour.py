n, lph = [int(d) for d in input().split()]
loc = sorted([int(input()) for _ in range(n)])
s, l = 0, 0
for v in loc:
    if l + v <= 5 * lph:
        l += v
        s += 1
    else:
        break
print(s)
