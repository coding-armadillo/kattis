w = input()
i = -1
while True:
    if w[i] in "aeiou":
        break
    i -= 1
print(w[: len(w) if i == -1 else i + 1] + "ntry")
