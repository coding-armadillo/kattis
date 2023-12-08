r, f = io.read("*n", "*n")

a = f // r
b = (f - a * r) / r >= 0.5 and 1 or 0

if (a + b) % 2 == 0 then
    print("up")
else
    print("down")
end
