n = int(input())
m = {}
for i in range(n):
    m[i] = [float(f) for f in input().split()]

for i in range(n):
    c = 0
    x, y = m[i][0], m[i][1]
    for j in range(n):
        if i == j:
            continue
        a, b, r = m[j]
        if round((x - a) ** 2 + (y - b) ** 2, 3) <= round(r**2, 3):
            c += 1
    print(c)
