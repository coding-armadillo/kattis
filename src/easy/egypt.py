while True:
    sides = sorted([int(d) for d in input().split()])
    if not all(sides):
        break
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("right")
    else:
        print("wrong")
