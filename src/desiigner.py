s = input()
if (
    s.startswith("b")
    and s[-1] in "aeiouy"
    and set(s[1:-1]) == {"r"}
    and len(s[1:-1]) >= 2
):
    print("Jebb")
else:
    print("Neibb")
