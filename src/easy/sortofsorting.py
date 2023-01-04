first = True
while True:
    n = int(input())
    if not n:
        break
    else:
        if not first:
            print()
    first = False
    names = []
    for _ in range(n):
        names.append(input())
    print("\n".join(sorted(names, key=lambda k: k[:2])))
