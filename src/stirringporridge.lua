t = io.read("*n")
l = 0
while true do
    if t - l >= l + 1 then
        t = t- l
        l = l+1
    else
        break
    end
end
print(l)
