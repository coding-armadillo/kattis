for i in range(int(input())):
    r, p, d = [int(d) for d in input().split()]
    recipe = {}
    main = None
    for _ in range(r):
        name, weight, percent = input().split()
        weight = float(weight)
        percent = float(percent)
        if percent == 100.0:
            main = name
        recipe[name] = (weight, percent)
    scale = d / p
    print(f"Recipe # {i+1}")
    dw = recipe[main][0] * scale
    for k in recipe:
        print(k, f"{recipe[k][1] * dw / 100:.1f}")
    print("-" * 40)
