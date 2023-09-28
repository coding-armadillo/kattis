mapping = {
    "th": "thou",
    "in": "inch",
    "ft": "foot",
    "yd": "yard",
    "ch": "chain",
    "fur": "furlong",
    "mi": "mile",
    "lea": "league",
}
names = list(mapping.values())
scale = [1, 1000, 12, 3, 22, 10, 8, 3]

v, a, _, b = input().split()
v = int(v)
na, nb = mapping.get(a, a), mapping.get(b, b)
ia, ib = names.index(na), names.index(nb)

rate = 1
for s in scale[min(ia, ib) + 1 : max(ia, ib) + 1]:
    rate *= s

print(v * rate if ia > ib else v / rate)
