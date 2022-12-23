s = input()

i = 0
size = len(s)
while i < size:
    if s[i] in [":", ";"]:
        if i + 1 < size and s[i + 1] == ")":
            print(i)
            i += 2
            continue
        if i + 2 < size and s[i + 1] == "-" and s[i + 2] == ")":
            print(i)
            i += 3
            continue

    i += 1
