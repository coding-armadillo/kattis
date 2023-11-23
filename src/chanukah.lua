for _ = 1, io.read("*n") do
    k, n = io.read("*n", "*n")
    print(k, math.floor((1 + n) * n / 2 + n))
end
