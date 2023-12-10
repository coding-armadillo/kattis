a, b, c, d, t = io.read("*n", "*n", "*n", "*n", "*n")
m = math.abs(a - c) + math.abs(b - d)
if m <= t and (m - t) % 2 == 0 then
    print("Y")
else
    print("N")
end
