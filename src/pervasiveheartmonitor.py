while True:
    try:
        line = input().split()
    except:
        break

    name, rate = [], []
    for p in line:
        if p.isalpha():
            name.append(p)
        else:
            rate.append(float(p))
    name = " ".join(name)
    rate = sum(rate) / len(rate)
    print(f"{rate:.6f} {name}")
