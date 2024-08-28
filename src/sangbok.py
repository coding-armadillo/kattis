t, n = [int(d) for d in input().split()]
s = sorted([int(d) for d in input().split()])
res = 0
for v in s:
    if res + v > t * 60:
        break
    res += v
print(res)
