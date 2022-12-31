n, t = [int(d) for d in input().split()]
p = [int(input()) for _ in range(n)]
p = sorted(p, reverse=True)
ending = p[0]
able = True
for i in range(1, n):
    if t * i >= ending:
        print("NO")
        able = False
        break
    if t * i + p[i] < ending:
        ending = t * i + p[i]
if able:
    print("YES")
