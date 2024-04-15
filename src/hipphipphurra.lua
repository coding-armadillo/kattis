n = io.read()
d = io.read("*n")
for _ = 1, d do
    print(string.format("Hipp hipp hurra, %s!", n))
end
