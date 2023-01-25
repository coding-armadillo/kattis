mapping = {"fat": 9, "protein": 4, "sugar": 4, "starch": 4, "alcohol": 7}


def c(x, category):
    if "g" in x:
        return (int(x[:-1]) * mapping[category], "C")
    elif "C" in x:
        return (int(x[:-1]), "C")
    elif "%" in x:
        return (int(x[:-1]) / 100, "%")


def solve(items):
    fat_c, total_c = 0, 0
    for fat, protein, sugar, starch, alcohol in items:
        fat_c += fat
        total_c += fat + protein + sugar + starch + alcohol

    return f"{fat_c/total_c:.0%}"


items = []
while True:
    s = input()
    if s == "-":
        if not items:
            break
        print(solve(items))

        items = []
        continue

    fat, protein, sugar, starch, alcohol = s.split()
    mapping.keys()

    total_c, total_p = 0, 0

    reading = []
    for v, k in zip(s.split(), mapping.keys()):
        n, t = c(v, k)
        if t == "C":
            total_c += n
        elif t == "%":
            total_p += n
        reading.append((n, t))

    total_c = total_c / (1 - total_p)

    item = []
    for n, t in reading:
        if t == "%":
            item.append(n * total_c)
        else:
            item.append(n)

    items.append(item)
