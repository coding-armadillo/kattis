s = [0, 0]
n = int(input())
v = []
for t in input().split():
    d = t[0]
    a = int(t[1:])
    if d == "N":
        s[1] += a
    elif d == "S":
        s[1] -= a
    elif d == "E":
        s[0] += a
    else:
        s[0] -= a
    v.append(list(s))
area = 0
for i in range(n):
    area += v[i][0] * v[(i + 1) % n][1] - v[i][1] * v[(i + 1) % n][0]
print(f"THE AREA IS {abs(area) // 2}")
