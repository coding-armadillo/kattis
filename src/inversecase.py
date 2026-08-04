import string

s = input()
i = []
for c in s:
    if c in string.ascii_lowercase:
        i.append(c.upper())
    elif c in string.ascii_uppercase:
        i.append(c.lower())
    else:
        i.append(c)
print("".join(i))
