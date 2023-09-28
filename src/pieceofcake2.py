n, h, v = [int(d) for d in input().split()]
print(4 * max(h * v, (n - h) * (n - v), h * (n - v), v * (n - h)))
