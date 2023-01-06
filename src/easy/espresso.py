n, s = [int(d) for d in input().split()]
refill = 0
tank = s
for _ in range(n):
    o = input()
    if "L" in o:
        w = int(o[:-1]) + 1
    else:
        w = int(o)
    if tank - w < 0:
        refill += 1
        tank = s

    tank -= w
print(refill)
