a, b, c = sorted([int(d) for d in input().split()])
if c - b == b - a:
    print(c + c - b)
elif c - b > b - a:
    print(c - b + a)
else:
    print(a + c - b)
