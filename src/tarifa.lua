x = io.read("*n")
n = io.read("*n")
local used = 0
for i = 1, n do
    used = used + io.read("*n")
end
print(x * (n + 1) - used)
