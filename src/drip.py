s, m, n = [int(d) for d in input().split()]
for _ in range(n):
    r = input().split()
    if r[0] == "DRIP":
        p = int(r[2])
        d = int(r[1]) * s
        s += d // p
        m += d % p
    elif r[0] == "NDRIP":
        p = int(r[1])
        ns = m // p
        s += ns
        m -= ns * p
print(s)
print(m)
