t = [int(d) for d in input()]
b = [f"{d:b}".zfill(4) for d in t]

for r in range(4):
    row = ["." if b[i][r] == "0" else "*" for i in range(4)]
    row.insert(2, " ")
    print(" ".join(row))
