n = io.read("*n")
d = 1
while 2 ^ (d - 1) < n do
    d = d + 1
end
print(d)
