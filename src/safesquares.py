b = []
for _ in range(8):
    b.append(list(input()))

s = []

for i in range(8):
    if "R" in b[i]:
        s.append(["R"] * 8)
    else:
        s.append(["."] * 8)

for i in range(8):
    if "R" in [b[j][i] for j in range(8)]:
        for j in range(8):
            s[j][i] = "R"

c = 0
for i in range(8):
    for j in range(8):
        if s[i][j] == ".":
            c += 1

print(c)
