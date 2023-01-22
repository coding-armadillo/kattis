k = input()
b = []
while True:
    line = input()
    if line == "-1":
        break
    b.append(line.split())

p = [k]
t = k
while True:
    found = False
    for row in b:
        if t in row[1:]:
            p.append(row[0])
            found = True
            t = row[0]
            break
    if not found:
        break

print(" ".join(p))
