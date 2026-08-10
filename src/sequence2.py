n = int(input())
a = []
for i in range(1, n + 1):
    if i in [1, 2, 3]:
        a.append(i)
    else:
        a.append(sum(a[-3:]))
print(*a, sep="\n")
