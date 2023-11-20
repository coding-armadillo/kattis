k = io.read("*n")
local a, b = 1, 0
for i = 1, k do
    a, b = b, b + a
end
print(a, b)
