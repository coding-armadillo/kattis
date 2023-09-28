c = {}
while True:
    try:
        s = input()
    except:
        break
    parts = s.split()
    if parts[0] == "define":
        v, n = parts[1:]
        c[n] = int(v)
    elif parts[0] == "eval":
        x, y, z = parts[1:]
        if x not in c or z not in c:
            print("undefined")
        elif y == "=":
            print("true" if c[x] == c[z] else "false")
        elif y == ">":
            print("true" if c[x] > c[z] else "false")
        elif y == "<":
            print("true" if c[x] < c[z] else "false")
