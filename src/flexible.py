w, p = [int(d) for d in input().split()]
l = [int(d) for d in input().split()]
l = [0] + l + [w]
c = set()
for i in range(p + 1):
    for j in range(i + 1, p + 2):
        c.add(l[j] - l[i])
print(" ".join([str(d) for d in sorted(c)]))
