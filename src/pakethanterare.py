t, b = [int(d) for d in input().split()]
s = [int(d) for d in input().split()]
p = {}
for _ in range(t):
    k, v = input().split()
    v = int(v)
    p[k] = v
for n in s:
    res = 0
    for _ in range(n):
        k, v = input().split()
        v = int(v)
        res += p[k] - v
    print(res)
