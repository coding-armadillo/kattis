n = int(input())
x = int(input())
y = int(input())
l = sorted([int(d) for d in input().split()])

total, c = 0, 0
for d in l:
    if (total + d * x) / (c + 1) <= y:
        total += d * x
        c += 1
    else:
        break
print(c)
