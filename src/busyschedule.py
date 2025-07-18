def f(s):
    hm, z = s.split()
    h, m = [int(d) for d in hm.split(":")]
    return (z, h % 12, m)


while True:
    n = int(input())
    if not n:
        break
    t = [input() for _ in range(n)]
    print(*sorted(t, key=lambda v: f(v)), sep="\n")
    print()
