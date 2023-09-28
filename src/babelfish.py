d = []
while True:
    line = input()
    if not line:
        break
    w, f = line.split()
    d.append((f, w))

d = dict(d)
while True:
    try:
        line = input()
    except:
        break
    print(d.get(line, "eh"))
