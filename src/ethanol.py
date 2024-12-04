n = int(input())
a = [" "] + ["H"] * n + [" "]
b = [" "] + ["|"] * n + [" "]
c = ["H"] + ["C"] * n + ["OH"]
print(" ".join(a))
print(" ".join(b))
print("-".join(c))
print(" ".join(b))
print(" ".join(a))
