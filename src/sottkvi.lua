n, k, today = io.read("*n", "*n", "*n")
res = 0
for _ = 1, n do
    d = io.read("*n")
    if d + 14 - today <= k then
        res = res + 1
    end
end
print(res)
