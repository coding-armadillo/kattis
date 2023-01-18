d = ["North", "East", "South", "West"]
a, b, c = input().split()
ia = d.index(a)
ib = d.index(b)
ic = d.index(c)

ib = (ib - ia) % 4
ic = (ic - ia) % 4
ia -= ia

if ib == 2:
    print("Yes" if ic == 3 else "No")
elif ib == 1:
    print("Yes" if ic in [2, 3] else "No")
else:
    print("No")
