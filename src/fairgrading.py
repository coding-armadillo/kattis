x, y, z = [int(d) for d in input().split()]
s = 0.25 * x + 0.25 * y + 0.5 * z
if s >= 90:
    print("A")
elif s >= 80:
    print("B")
elif s >= 70:
    print("C")
elif s >= 60:
    print("D")
else:
    print("F")
