n = int(input())
mapping = {}
for _ in range(n):
    names = input().split()
    mapping[names[0]] = names
m = int(input())
for _ in range(m):
    name = input()
    if name not in mapping:
        print("Neibb")
    elif name in mapping and len(mapping[name]) == 1:
        print("Jebb")
    else:
        print(f'Neibb en {" ".join(mapping[name])} er heima')
