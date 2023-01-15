while True:
    try:
        s = input()
    except:
        break
    parts = []
    prev, t = s[0], 1
    for c in s[1:]:
        if c != prev:
            parts.append((prev, t))
            t = 1
            prev = c
        else:
            t += 1
    parts.append((prev, t))
    print("".join([f"{v}{k}" for k, v in parts]))
