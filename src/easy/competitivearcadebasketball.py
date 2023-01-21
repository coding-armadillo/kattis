from collections import Counter

n, p, m = [int(d) for d in input().split()]

records = Counter()
winners = []
names = [input() for _ in range(n)]
for r in range(m):
    name, point = input().split()
    point = int(point)
    records[name] += point
    if records[name] >= p and name not in winners:
        winners.append(name)
if not winners:
    print("No winner!")
else:
    print("\n".join([f"{n} wins!" for n in winners]))
