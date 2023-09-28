while True:
    n = input()
    if n == "0":
        break
    s1 = sum([int(d) for d in n])

    n = int(n)
    p = 11
    while True:
        s2 = sum([int(d) for d in str(n * p)])
        if s2 == s1:
            break
        p += 1

    print(p)
