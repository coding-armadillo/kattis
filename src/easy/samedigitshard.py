a, b = [int(d) for d in input().split()]
pairs = []
for x in range(a, b + 1):
    for y in range(x, b + 1):
        xy = x * y
        if x * y > b:
            break
        if sorted(str(xy)) == sorted(str(x) + str(y)):
            pairs.append((x, y, xy))
    if x * x > b:
        break

print(f"{len(pairs)} digit-preserving pair(s)")
for x, y, xy in pairs:
    print(f"x = {x}, y = {y}, xy = {xy}")
