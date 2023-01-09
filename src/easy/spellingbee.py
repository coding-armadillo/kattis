hexagon = input()
c = hexagon[0]
hexagon = set(list(hexagon))
n = int(input())
valid = []
for _ in range(n):
    w = input()
    if c in w and len(w) >= 4 and set(list(w)) <= hexagon:
        valid.append(w)
print("\n".join(valid))
