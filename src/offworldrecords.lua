n, c, p = io.read("*n", "*n", "*n")
ans = 0
for _ = 1, n do
    h = io.read("*n")
    if h > c + p then
        ans = ans + 1
        c, p = h, c
    end
end
print(ans)
