r, g, b = [int(d) for d in input().split()]
if r > g and r > b:
    print("raudur")
elif g > r and g > b:
    print("graenn")
elif b > r and b > g:
    print("blar")
elif r == g and b < g:
    print("gulur")
elif r == b and g < b:
    print("fjolubleikur")
elif b == g and r < b:
    print("blagraenn")
elif r == g and g == b and b == 0:
    print("svartur")
elif r == g and g == b and b == 255:
    print("hvitur")
elif r == g and g == b:
    print("grar")
else:
    print("othekkt")
