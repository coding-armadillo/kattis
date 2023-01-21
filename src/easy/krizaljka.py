a, b = input().split()
for i in range(len(a)):
    if a[i] in b:
        j = b.index(a[i])
        break

rows = []

for k in range(j):
    rows.append("." * i + b[k] + "." * (len(a) - i - 1))

rows.append(a)

for k in range(j + 1, len(b)):
    rows.append("." * i + b[k] + "." * (len(a) - i - 1))

print("\n".join(rows))
