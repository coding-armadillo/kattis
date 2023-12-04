n = io.read("*n")
s = 0
b = 0
for _ = 1, n do
    t = io.read("*n")
    if t > 0 then
        b = b + t
    elseif b + t < 0 then
        s = s - (b + t)
        b = 0
    else
        b = b + t
    end
end
print(s)
