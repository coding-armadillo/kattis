for _ = 1, io.read("*n") do
    a, b, c = io.read("*n", "*n", "*n")
    if a + b == c or a * b == c or a - b == c or b - a == c or a == b * c or b == a * c then
        print("Possible")
    else
        print("Impossible")
    end
end
