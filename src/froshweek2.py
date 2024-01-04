_ = input()
t = sorted([int(d) for d in input().split()])
l = sorted([int(d) for d in input().split()])
i = 0
for d in l:
    if t[i] <= d:
        i += 1
print(i)
