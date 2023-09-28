while True:
    try:
        m, p, l, e, r, s, n = [int(d) for d in input().split()]
    except:
        break
    for _ in range(n):
        pp = p
        p = l // r
        l = e * m
        m = pp // s
    print(m)
