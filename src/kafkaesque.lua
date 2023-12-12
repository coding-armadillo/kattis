n = io.read("*n")
t, c = 0, 1
for _ = 1, n do
    v = io.read("*n")
    if v < t then
        t = 0
        c = c + 1
    end
    t = v
end
print(c)
