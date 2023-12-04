a, b, h = io.read("*n", "*n", "*n")
t = 0
while h >= 0 do
    h = h - a
    t = t + 1
    if h <= 0 then
        break
    end
    h = h + b
end
print(t)
