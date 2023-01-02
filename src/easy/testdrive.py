a, b, c = [int(d) for d in input().split()]
x, y = b - a, c - b
if x == y:
    print("cruised")
elif x * y < 0:
    print("turned")
elif abs(y) > abs(x):
    print("accelerated")
else:
    print("braked")
