g, r = [int(d) for d in input().split()]
ans = 0
if g > 0:
    ans += 10 * min(g, r)
    remain = max(g - r, 0)
    ans += 10 * (remain // 3)
    remain %= 3
    ans += 3 * (remain // 2)
    remain %= 2
    ans += remain
print(ans)
