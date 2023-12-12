n = io.read("*n")
ceil = math.ceil(n / 100) * 100 - 1
floor = math.floor(n / 100) * 100 - 1
if math.abs(ceil - n) <= math.abs(n - floor) or floor < 0 then
    print(ceil)
else
    print(floor)
end
