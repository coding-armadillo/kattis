n = io.read("*n")
total = 0
for i = 1, n do
    total = total + io.read("*n")
end
if total % 3 > 0 then
    print("no")
else
    print("yes")
end
