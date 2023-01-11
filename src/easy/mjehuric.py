f = input().split()
while f != [str(d) for d in range(1, 6)]:
    for i in range(4):
        if f[i] > f[i + 1]:
            f[i], f[i + 1] = f[i + 1], f[i]
            print(" ".join(f))
