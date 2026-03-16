while True:
    l = input()
    if l.startswith("0"):
        break
    n = l.split()[1:]
    s = None
    v = []
    for d in n:
        if d != s:
            v.append(d)
            s = d
    print(" ".join(v), "$")
