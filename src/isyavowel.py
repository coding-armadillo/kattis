w = input()
a, b = 0, 0
for c in w:
    if c in "aeiou":
        a += 1
    if c == "y":
        b += 1
print(a, a + b)
