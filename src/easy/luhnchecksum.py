for _ in range(int(input())):
    n = input()[::-1]
    checksum = 0
    for i in range(len(n)):
        s = int(n[i]) * (i % 2 + 1)
        if s > 9:
            s = sum([int(d) for d in str(s)])
        checksum += s

    print("FAIL" if checksum % 10 else "PASS")
