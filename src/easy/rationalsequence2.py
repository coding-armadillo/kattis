def f(l, r):
    if l == r:
        return 1
    elif l > r:
        return 2 * f(l - r, r) + 1
    else:
        return 2 * f(l, r - l)


for _ in range(int(input())):
    k, v = input().split()
    l, r = [int(d) for d in v.split("/")]
    print(f"{k} {f(l,r)}")
