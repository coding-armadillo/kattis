a, b, h = [int(d) for d in input().split()]
t = 0
while h >= 0:
    h -= a
    t += 1
    if h <= 0:
        break
    h += b
print(t)
