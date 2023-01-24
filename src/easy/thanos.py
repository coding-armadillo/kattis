for _ in range(int(input())):
    p, r, f = [int(d) for d in input().split()]
    y = 0
    while p <= f:
        p *= r
        y += 1
    print(y)
