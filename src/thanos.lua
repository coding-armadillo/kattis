for _ = 1, io.read("*n") do
    p, r, f = io.read("*n", "*n", "*n")
    y = 0
    while p <= f do
        p = p * r
        y = y + 1
    end
    print(y)
end
