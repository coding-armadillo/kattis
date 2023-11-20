n = io.read("*n")
d = 0
for i = 1, n do
    x, y = io.read("*n", "*n")
    d = d + 2 * (x - y)
end
print(-d / (2 * n))
