while True:
    a, b = [int(d) for d in input().split()]
    if a < b:
        print("Less")
    elif a > b:
        print("More")
    else:
        break
