n, q = [int(d) for d in input().split()]
m = {}
for _ in range(n):
    name = input()
    init = "".join([p[0] for p in name.split()])
    if init not in m:
        m[init] = name
    else:
        m[init] = "ambiguous"
for _ in range(q):
    print(m.get(input(), "nobody"))
