x1, y1 = io.read("*n", "*n")
x2, y2 = io.read("*n", "*n")
x3, y3 = io.read("*n", "*n")

d12 = (x1 - x2) ^ 2 + (y1 - y2) ^ 2
d13 = (x1 - x3) ^ 2 + (y1 - y3) ^ 2
d23 = (x2 - x3) ^ 2 + (y2 - y3) ^ 2

if d12 == d13 then
    x, y = x2 + x3 - x1, y2 + y3 - y1
elseif d12 == d23 then
    x, y = x1 + x3 - x2, y1 + y3 - y2
else
    x, y = x1 + x2 - x3, y1 + y2 - y3
end
print(x, y)
