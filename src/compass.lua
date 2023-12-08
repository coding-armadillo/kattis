n1, n2 = io.read("*n", "*n")
d = (n2 - n1) % 360
if d > 180 then
    d = d - 360
end
print(d)
