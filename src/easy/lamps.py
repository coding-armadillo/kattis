h, p = [int(d) for d in input().split()]

days = 0
cost_bulb, cost_lamp = 5, 60
used_bulb, used_lamp = 0, 0

while True:
    days += 1
    cost_bulb += 60 * h * p / 100000
    cost_lamp += 11 * h * p / 100000
    used_bulb += h
    used_lamp += h

    if used_bulb > 1000:
        cost_bulb += 5
        used_bulb -= 1000

    if used_lamp > 8000:
        cost_lamp += 60
        used_lamp -= 8000

    if cost_bulb > cost_lamp:
        break

print(days)
