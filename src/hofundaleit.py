n, q = [int(d) for d in input().split()]
b = []
for _ in range(n):
    t, a = input().split(", ")
    b.append((t, a))

b = dict(zip([t for t, _ in sorted(b, key=lambda v: (v[1], v[0]))], range(1, n + 1)))

for _ in range(q):
    t = input()
    print(b.get(t, -1))
