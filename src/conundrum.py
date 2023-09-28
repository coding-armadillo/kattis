text = input()
total = 0
for i in range(0, len(text), 3):
    if text[i] != "P":
        total += 1
    if text[i + 1] != "E":
        total += 1
    if text[i + 2] != "R":
        total += 1
print(total)
