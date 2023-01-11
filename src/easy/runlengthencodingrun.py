action, s = input().split()
if action == "D":
    print("".join([s[i] * int(s[i + 1]) for i in range(0, len(s), 2)]))
elif action == "E":
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

    print("".join([f"{k}{v}" for k, v in parts]))
