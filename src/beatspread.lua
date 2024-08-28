for _ = 1, io.read("*n") do
    a, b = io.read("*n", "*n")
    if a < b or (a + b) % 2 == 1 then
        print("impossible")
    else
        print((a + b) // 2, (a - b) // 2)
    end
end
