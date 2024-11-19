g, r = io.read("*n", "*n")
ans = 0
if g > 0 then
    ans = ans + 10 * math.min(g, r)
    remain = math.max(g - r, 0)
    ans = ans + 10 * (remain // 3)
    remain = remain % 3
    ans = ans + 3 * (remain // 2)
    remain = remain % 2
    ans = ans + remain
end
print(ans)
