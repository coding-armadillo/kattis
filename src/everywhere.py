cities = {}
for i in range(int(input())):
    cities[i] = set()
    for _ in range(int(input())):
        cities[i].add(input())

print("\n".join([str(len(s)) for s in cities.values()]))
