n = io.read("*n")
c, m = 0, 0
for _ = 1, n do
    a, b = io.read("*n", "*n")
    c = c + b - a
    m = math.max(m, c)
end
print(m)
