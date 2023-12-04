b, k, g = io.read("*n", "*n", "*n")
b = b - 1
d = b // (k // g)
if b % (k // g) > 0 then
    d = d + 1
end
print(d)
