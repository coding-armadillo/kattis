y, p = input().split()
if y.endswith("e"):
    name = y + "x" + p
elif y[-1] in "aiou":
    name = y[:-1] + "ex" + p
elif y.endswith("ex"):
    name = y + p
else:
    name = y + "ex" + p

print(name)
