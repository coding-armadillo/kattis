y = io.read("*n")
if 26 - ((y - 2018) * 12 - 4) % 26 <= 12 then
    print("YES")
else
    print("NO")
end
