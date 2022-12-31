n, p, q = [int(d) for d in input().split()]

if ((p + q) // n) % 2 == 0:
    print("paul")
else:
    print("opponent")
