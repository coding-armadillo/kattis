s, p = [int(d) for d in input().split()]
t = 0
while True:
    t += s
    m = t * p / 100
    if abs(m - s) < 10e-7:
        break
    t -= m
print(t)
