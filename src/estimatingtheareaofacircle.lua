while true do
    r, m, c = io.read("*n", "*n", "*n")
    if r == 0 and m == 0 and c == 0 then
        break
    end
    print(math.pi * r * r, 4 * r * r * c / m)
end
