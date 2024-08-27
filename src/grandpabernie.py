n = int(input())
m = {}
for _ in range(n):
    c, y = input().split()
    y = int(y)
    if c not in m:
        m[c] = [y]
    else:
        m[c].append(y)
for c in m:
    m[c] = sorted(m[c])
q = int(input())
for _ in range(q):
    c, i = input().split()
    print(m[c][int(i) - 1])
