a, b, c = int(input()), int(input()), int(input())
t = b * b - 4 * a * c
if t < 0:
    print(0)
elif t == 0:
    print(1)
else:
    print(2)
