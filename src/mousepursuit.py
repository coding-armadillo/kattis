n = int(input())
e = []
for _ in range(n):
    a, s, c, g = input().split()
    s = int(s)
    c = int(c) if a == "CAUGHT" else -int(c)
    g = int(g) if a == "CAUGHT" else -int(g)
    e.append((s, c, g))

k = int(input())
e = [t for t in e if t[0] <= k]

print(sum(t[1] for t in e), sum(t[2] for t in e))
