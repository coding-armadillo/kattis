for _ in range(int(input())):
    r, e, c = [int(d) for d in input().split()]
    if e > r + c:
        print("advertise")
    elif e < r + c:
        print("do not advertise")
    else:
        print("does not matter")
