a, b = io.read("*n", "*n")
c = a % b
print(math.min(c, b - c))
