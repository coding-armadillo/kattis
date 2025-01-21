f, h = input(), input()
i, j = 0, 0
while j < len(h):
    if h[j] == f[i]:
        i += 1
        if i == len(f):
            break
    j += 1
print("Ja" if i == len(f) else "Nej")
