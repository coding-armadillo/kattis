n = int(input())
lsc = [input() for _ in range(n)]
m = int(input())
for _ in range(m):
    if any([input() in lsc for _ in range(6)]):
        print("Hæfileikalaust Drasl")
    else:
        print("Fínn Stokkur")
