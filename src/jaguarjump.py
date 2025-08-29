w, h, d = [int(n) for n in input().split()]
c, j = None, None
for i in range(h):
    s = input()
    if "@" in s:
        c = (i, s.index("@"))
    if "J" in s:
        j = (i, s.index("J"))
print(
    "no jumpscares here"
    if (c[0] - j[0]) ** 2 + (c[1] - j[1]) ** 2 > d**2
    else "the guide is right"
)
