n = int(input())
a = [int(d) for d in input().split()]

g = [a[0]]
for i in range(1, n):
    v = a[i]
    if v > g[-1]:
        g.append(v)
print(len(g))
print(" ".join([str(d) for d in g]))
