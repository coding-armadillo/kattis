a, b = io.read("*n", "*n")
va, vb = 0, 0
for _ = 1, a do
    c, v = io.read("*n", "*n")
    va = va + c * v
end
for _ = 1, b do
    c, v = io.read("*n", "*n")
    vb = vb + c * v
end
if va == vb then
    print("same")
else
    print("different")
end
