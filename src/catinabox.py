h, w, l, c = [int(d) for d in input().split()]
v = h * w * l
if v == c:
    print("COZY")
elif v > c:
    print("SO MUCH SPACE")
else:
    print("TOO TIGHT")
