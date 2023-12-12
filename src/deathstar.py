n = int(input())
a = [0] * n
for i in range(n):
    m = [int(d) for d in input().split()]
    for v in m:
        a[i] |= v
print(" ".join([str(d) for d in a]))
