n1, n2 = int(input()), int(input())
d = (n2 - n1) % 360
if d > 180:
    d -= 360
print(d)
