g, s, c = [int(d) for d in input().split()]

buying = 3 * g + 2 * s + 1 * c
result = []

if buying >= 8:
    result.append("Province")
elif buying >= 5:
    result.append("Duchy")
elif buying >= 2:
    result.append("Estate")

if buying >= 6:
    result.append("Gold")
elif buying >= 3:
    result.append("Silver")
else:
    result.append("Copper")

print(" or ".join(result))
