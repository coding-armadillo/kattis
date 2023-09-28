_, a = [int(d) for d in input().split()]
e = sorted([int(d) + 1 for d in input().split()])

t = 0
for s in e:
    if a >= s:
        t += 1
        a -= s
    else:
        break
print(t)
