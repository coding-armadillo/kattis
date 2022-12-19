size = {}
for _ in range(int(input())):
    parts = input().split()
    if parts[0].isdigit():
        size[parts[1]] = int(parts[0]) / 2
    else:
        size[parts[0]] = int(parts[1])
for color in sorted(size, key=lambda x: size[x]):
    print(color)
