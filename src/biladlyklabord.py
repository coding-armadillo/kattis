s = input()
p = s[0]
print(p, end="")
for c in s[1:]:
    if c != p:
        print(c, end="")
    p = c
