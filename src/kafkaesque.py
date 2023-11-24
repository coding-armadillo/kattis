n = int(input())
t, c = 0, 1
for _ in range(n):
    v = int(input())
    if v < t:
        t = 0
        c += 1
    t = v
print(c)
