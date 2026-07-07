from collections import Counter

while True:
    s = input()
    if s == "#":
        break
    else:
        r = s[-1]
        c = Counter(s[:-1])
        if r == "e":
            print(f"{s[:-1]}{'1' if c['1'] % 2 else '0'}")
        else:
            print(f"{s[:-1]}{'0' if c['1'] % 2 else '1'}")
