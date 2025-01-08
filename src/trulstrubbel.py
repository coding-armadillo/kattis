s, t, h = input(), 0, 0
for c in s:
    if c == "T":
        t += 1
    else:
        h += 1
    if abs(t - h) >= 2 and (t >= 11 or h >= 11):
        v = max(11, min(t, h) + 2)
        t = max(t - v, 0)
        h = max(h - v, 0)
print(f"{t}-{h}")
