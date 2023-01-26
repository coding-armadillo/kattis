context = {}
while True:
    s = input()
    if s == "0":
        break

    if "=" in s:
        x, y = [d.strip() for d in s.split("=")]
        context[x] = int(y)
    else:
        v = [d.strip() for d in s.split("+")]
        t = 0
        n = []
        for d in v:
            if d.isdigit():
                t += int(d)
            elif d in context:
                t += context[d]
            else:
                n.append(d)
        if len(n) < len(v):
            n = [str(t)] + n
        print(" + ".join(n))
