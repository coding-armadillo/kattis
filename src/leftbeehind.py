while True:
    x, y = [int(d) for d in input().split()]
    if not x and not y:
        break
    if x + y == 13:
        print("Never speak again.")
    elif x > y:
        print("To the convention.")
    elif x == y:
        print("Undecided.")
    else:
        print("Left beehind.")
