xp, yp = [int(d) for d in input().split()]
xv, yv = [int(d) for d in input().split()]
u = int(input())
d = (xp - xv) ** 2 + (yp - yv) ** 2
if d == u:
    print("on the fence")
elif d < u:
    print("for")
else:
    print("against")
