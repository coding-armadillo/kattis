n, v = io.read("*n", "*n")
b = {}
for i = 1, n do
    l, w, h = io.read("*n", "*n", "*n")
    b[i] = (l * w * h)
end
print(math.max(table.unpack(b)) - v)
