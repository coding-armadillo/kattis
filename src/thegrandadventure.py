mapping = {"b": "$", "t": "|", "j": "*"}
for _ in range(int(input())):
    a = input()
    bag = []
    early_fail = False
    for i in a:
        if i in mapping.values():
            bag.append(i)
        elif i in mapping:
            if not bag or bag.pop() != mapping[i]:
                print("NO")
                early_fail = True
                break
    if not early_fail:
        print("YES" if not bag else "NO")
