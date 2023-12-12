l, r = io.read("*n", "*n")
if l == 0 and r == 0 then
    print("Not a moose")
else
    p = 2 * math.max(l, r)
    if l ~= r then
        print("Odd", p)
    else
        print("Even", p)
    end
end
