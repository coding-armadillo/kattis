n = int(input())
ans = []
for _ in range(n):
    p = input().split()
    if len(p) == 1:
        ans.append(0)
    else:
        v = 0
        for i in range(len(p) - 1):
            a, b = p[i].split("-")[1], p[i + 1].split("-")[0]
            ha, sa = [int(d) for d in a.split(":")]
            hb, sb = [int(d) for d in b.split(":")]
            v += (hb - ha) * 60 + (sb - sa)
        ans.append(v)
print(0 if 0 in ans else min(ans))
