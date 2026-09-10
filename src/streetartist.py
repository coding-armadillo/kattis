n = int(input())
s = []
for _ in range(n):
    name, height = input().split()
    height = int(height)
    s.append((name, height))
s = s[::-1]
v = [s[0]]
for p in s[1:]:
    if p[1] > v[-1][1]:
        v.append(p)
print(" ".join(p[0] for p in sorted(v, key=lambda p: -p[1])))
