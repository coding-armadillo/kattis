a, b = [int(d) for d in input().split()]
n = int(input())
shields = []
for _ in range(n):
    l, u, f = input().split()
    l = int(l)
    u = int(u)
    f = float(f)
    shields.append((l, u, f))

shields.append((b,))
s = shields[0][0]
for i in range(n):
    s += (shields[i][1] - shields[i][0]) * shields[i][2]
    s += shields[i + 1][0] - shields[i][1]
print(f"{a/s:.6f}")
