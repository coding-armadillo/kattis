m = {}
for k in "cdefgabCDEFGAB":
    m[k] = [False] * 10
for f in list(range(1, 4)) + list(range(6, 10)):
    m["c"][f] = True
for f in list(range(1, 4)) + list(range(6, 9)):
    m["d"][f] = True
for f in list(range(1, 4)) + list(range(6, 8)):
    m["e"][f] = True
for f in list(range(1, 4)) + list(range(6, 7)):
    m["f"][f] = True
for f in range(1, 4):
    m["g"][f] = True
for f in range(1, 3):
    m["a"][f] = True
for f in range(1, 2):
    m["b"][f] = True
for f in range(2, 3):
    m["C"][f] = True
for f in list(range(0, 4)) + list(range(6, 9)):
    m["D"][f] = True
for f in list(range(0, 4)) + list(range(6, 8)):
    m["E"][f] = True
for f in list(range(0, 4)) + list(range(6, 7)):
    m["F"][f] = True
for f in range(0, 4):
    m["G"][f] = True
for f in range(0, 3):
    m["A"][f] = True
for f in range(0, 2):
    m["B"][f] = True

for _ in range(int(input())):
    notes = input()
    c = [0] * 10
    p = [False] * 10
    for n in notes:
        for i, f in enumerate(m[n]):
            if f and not p[i]:
                c[i] += 1
                p[i] = f
            elif not f and p[i]:
                p[i] = f
            else:
                pass
    print(*c)
