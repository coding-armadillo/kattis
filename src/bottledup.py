s, v1, v2 = [int(d) for d in input().split()]

n1 = s // v1
if not s % v1:
    print(n1, 0)
else:
    while True:
        if not (s - n1 * v1) % v2:
            print(n1, (s - n1 * v1) // v2)
            break
        else:
            n1 -= 1
            if n1 < 0:
                break
    if n1 < 0:
        print("Impossible")
