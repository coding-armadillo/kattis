n = io.read("*n")
e = 1
m = 1.0
for i = 1, n do
    m = m * i
    e = e + 1 / m
end
print(string.format("%.12f", e))
