n, b = io.read("*n", "*n")
if (2 ^ (b + 1)) - 1 >= n then
    print("yes")
else
    print("no")
end
