s = input()
x, y = 0, 0
zoom = len(s)
for i in range(len(s)):
    d = 2 ** (zoom - i - 1)
    if s[i] == "1":
        x += d
    elif s[i] == "2":
        y += d
    elif s[i] == "3":
        x += d
        y += d
print(f"{zoom} {x} {y}")
