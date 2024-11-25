n = int(input())
s, d = "sober", 0
for _ in range(n):
    v = input()
    if v == "drunk" and s != "drunk":
        d += 1
    s = v
print(d)
