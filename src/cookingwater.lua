n = io.read("*n")
lb, ub = 0, 1000
for _ = 1, n do
    a, b = io.read("*n", "*n")
    lb = math.max(lb, a)
    ub = math.min(ub, b)
end
if lb > ub then
    print("edward is right")
else
    print("gunilla has a point")
end
