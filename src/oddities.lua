for _ = 1, io.read("*n") do
    x = io.read("*n")
    if x % 2 == 1 then
        ans = 'odd'
    else
        ans = 'even'
    end
    print(string.format("%d is %s", x, ans))
end
