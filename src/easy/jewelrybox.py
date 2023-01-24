def f(h):
    a = x - 2 * h
    b = y - 2 * h
    return a * b * h


for _ in range(int(input())):
    x, y = [int(d) for d in input().split()]
    h = (x + y - ((x + y) ** 2 - 3 * x * y) ** 0.5) / 6
    print(f"{f(h):.11f}")
