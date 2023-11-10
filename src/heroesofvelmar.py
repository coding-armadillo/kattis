m = {
    "Shadow": 6,
    "Gale": 5,
    "Ranger": 4,
    "Anvil": 7,
    "Vexia": 3,
    "Guardian": 8,
    "Thunderheart": 6,
    "Frostwhisper": 2,
    "Voidclaw": 3,
    "Ironwood": 3,
    "Zenith": 4,
    "Seraphina": 1,
}


def calculate(heros, location):
    boost = 0

    if "Seraphina" in heros:
        boost += heros.count("Seraphina") * (len(heros) - 1)

    if location == "center":
        boost += heros.count("Zenith") * 5

    if len(heros) == 4:
        boost += m["Thunderheart"] * heros.count("Thunderheart")

    return sum([m[h] for h in heros]) + boost


l1 = calculate(input().split()[1:], "left")
l2 = calculate(input().split()[1:], "left")
c1 = calculate(input().split()[1:], "center")
c2 = calculate(input().split()[1:], "center")
r1 = calculate(input().split()[1:], "right")
r2 = calculate(input().split()[1:], "right")

s1, s2 = 0, 0

if l1 > l2:
    s1 += 1
elif l1 < l2:
    s2 += 1

if c1 > c2:
    s1 += 1
elif c1 < c2:
    s2 += 1

if r1 > r2:
    s1 += 1
elif r1 < r2:
    s2 += 1

if s1 > s2:
    print("Player 1")
elif s1 < s2:
    print("Player 2")
else:
    if l1 + c1 + r1 > l2 + c2 + r2:
        print("Player 1")
    elif l1 + c1 + r1 < l2 + c2 + r2:
        print("Player 2")
    else:
        print("Tie")
