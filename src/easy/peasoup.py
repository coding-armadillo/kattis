found = False
for _ in range(int(input())):
    k = int(input())

    name = input()
    items = [input() for _ in range(k)]
    if "pea soup" in items and "pancakes" in items:
        found = True
        print(name)
        break

if not found:
    print("Anywhere is fine I guess")
