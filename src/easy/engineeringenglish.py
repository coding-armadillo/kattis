seen = set()

while True:
    try:
        s = input().split()
    except:
        break
    d = []
    for t in s:
        if t.lower() not in seen:
            seen.add(t.lower())
        else:
            t = "."
        d.append(t)
    print(" ".join(d))
