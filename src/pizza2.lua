r, c = io.read("*n", "*n")
print(string.format("%.6f", (r - c) ^ 2 / r ^ 2 * 100))
