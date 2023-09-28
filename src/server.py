_, t = [int(d) for d in input().split()]
total, used = 0, 0
for v in [int(d) for d in input().split()]:
    if used + v <= t:
        total += 1
        used += v
    else:
        break
print(total)
