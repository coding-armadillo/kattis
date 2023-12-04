n, h, v = io.read("*n", "*n", "*n")
print(4 * math.max(h * v, (n - h) * (n - v), h * (n - v), v * (n - h)))
