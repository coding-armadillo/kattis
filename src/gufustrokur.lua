a, b = io.read("*n", "*n")
v = math.abs(a - b)
print(math.min(v, 360 - v))
