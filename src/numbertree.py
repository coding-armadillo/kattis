items = input().split()
if len(items) == 2:
    h, s = items
else:
    h, s = items[0], ""

total, i = 2 ** (int(h) + 1), 1

for c in s:
    i *= 2
    if c == "R":
        i += 1

print(total - i)
