n = io.read("*n")
local min = math.huge
for i = 1, n do
    value = io.read("*n")
    min   = min < value and min or value
end
print(1 + min)
