n = io.read("*n")
length = 0
for _ = 1, n do
    length = length + io.read("*n")
end
length = length - (n - 1)
print(length)
