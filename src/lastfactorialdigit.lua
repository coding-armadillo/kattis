for _ = 1, io.read("*n") do
    n = io.read("*n")
    number = 1
    for i = 1, n do
        number = number * i
    end
    print(number % 10)
end
