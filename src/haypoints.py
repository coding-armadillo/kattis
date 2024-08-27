m, n = [int(d) for d in input().split()]
h = {}
for _ in range(m):
    k, v = input().split()
    h[k] = int(v)
for _ in range(n):
    res = 0
    while True:
        s = input()
        if s == ".":
            break
        w = s.split()
        res += sum(h.get(k, 0) for k in w)
    print(res)
