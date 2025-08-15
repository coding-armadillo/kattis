x, y, z = io.read("*n", "*n", "*n")
s = .25 * x + .25 * y + .5 * z
if s >= 90 then
    print("A")
elseif s >= 80 then
    print("B")
elseif s >= 70 then
    print("C")
elseif s >= 60 then
    print("D")
else
    print("F")
end
