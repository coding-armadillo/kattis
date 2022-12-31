while True:
    m, n = [int(d) for d in input().split()]
    if not m and not n:
        break
    a = m // n
    b = m % n
    print(f"{a} {b} / {n}")
