for _ in range(int(input())):
    n, m = [int(d) for d in input().split()]
    r = []
    for _ in range(n):
        s = input().split()
        p = int(s[-1])
        k = [int(d) for d in s[1:-1]]
        r.append((k, p))
    s = [int(d) for d in input().split()]

    ans = 0
    for t, p in r:
        c = min([s[d - 1] for d in t])
        ans += p * c

    print(ans)
