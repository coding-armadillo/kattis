name = {}
value = {}
op = ["-", "+"]
while True:
    try:
        s = input().split()
    except:
        break

    if s[0] == "clear":
        name.clear()
        value.clear()
    elif s[0] == "def":
        n, v = s[1:]
        v = int(v)
        if n in name:
            value.pop(name[n])
        name[n] = v
        value[v] = n
    elif s[0] == "calc":
        try:
            ans = eval("".join([str(name[p]) if p not in op else p for p in s[1:-1]]))
        except:
            ans = "unknown"

        ans = value.get(ans, "unknown")
        print(" ".join(s[1:] + [ans]))
