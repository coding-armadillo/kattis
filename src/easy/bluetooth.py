n = int(input())
cond = {}


def f(t):
    if t[0].isdigit():
        return (f'R{"u" if t[1]=="+" else "l"}', t[0])
    else:
        return (f'L{"u" if t[0]=="+" else "l"}', t[1])


for _ in range(n):
    t, p = input().split()
    q, d = f(t)
    if p == "b":
        if p not in cond:
            cond[p] = [q]
        else:
            cond[p].append(q)
    elif p == "m":
        if p not in cond:
            cond[p] = [(q, d)]
        else:
            cond[p].append((q, d))

l, r = True, True

if "R" in [c[0] for c in cond.get("b", [])]:
    r = False
if "L" in [c[0] for c in cond.get("b", [])]:
    l = False

ru = len([d for q, d in cond.get("m", []) if q == "Ru"])
rl = len([d for q, d in cond.get("m", []) if q == "Rl"])
lu = len([d for q, d in cond.get("m", []) if q == "Lu"])
ll = len([d for q, d in cond.get("m", []) if q == "Ll"])

if ru == 8 or rl == 8:
    r = False
if lu == 8 or ll == 8:
    l = False

if not l and not r:
    print(2)
elif l and not r:
    print(0)
elif r and not l:
    print(1)
else:
    print("?")
