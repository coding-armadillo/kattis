a, b, c = io.read("*n", "*n", "*n")
t = b * b - 4 * a * c
if t < 0 then
    print(0)
elseif t == 0 then
    print(1)
else
    print(2)
end
