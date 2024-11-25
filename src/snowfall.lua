n, h = io.read("*n"), 0
for _ = 1, n do
    t, a = io.read("*n", "*n")
    if t == 1 then
        h = math.max(h - a, 0)
    else
        h = h + a
    end
end
print(h)
