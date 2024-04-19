n, s = io.read("*n", "*n")
for _ = 1, n do
    a, b = io.read("*n", "*n")
    if s >= a and s <= b then
        s = s + 1
    end
end
print(s)
