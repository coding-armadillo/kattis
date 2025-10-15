n = int(input())
h = 0
t = 0
while True:
    if t + (h + 1) <= n:
        h += 1
        t += h
    else:
        break
print(h)
