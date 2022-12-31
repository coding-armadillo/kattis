p, n = [int(d) for d in input().split()]
boat = set()
d = -1
for i in range(n):
    w = input()
    boat.add(w)
    if len(boat) == p:
        d = i + 1
        break
if d == -1:
    print("paradox avoided")
else:
    print(d)
