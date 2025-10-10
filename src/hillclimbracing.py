l, a = [int(d) for d in input().split()]
h = [int(d) for d in input().split()]
f = True
for i in range(l):
    v = h[i + 1] - h[i]
    if v > 0 and v > a:
        f = False
print("POSSIBLE" if f else "BUG REPORT")
