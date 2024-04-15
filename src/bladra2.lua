v, a, t = io.read("*n", "*n", "*n")
print(string.format("%.5f", v * t + a * t * t / 2))
