l, r = [int(d) for d in input().split()]
if 2 * (l / 2) ** 2 <= r**2:
    print("fits")
else:
    print("nope")
