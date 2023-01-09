from itertools import permutations

l = []
while True:
    try:
        l.extend(input().split())
    except:
        break

w = set()
for i, j in permutations(l, 2):
    w.add(f"{i}{j}")


print("\n".join(sorted(w)))
