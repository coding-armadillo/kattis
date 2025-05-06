xb, yb = io.read("*n", "*n")
n = io.read("*n")
safe = true
for _ = 1, n do
    xa, ya = io.read("*n", "*n")
    if (xa - xb) * (xa - xb) + (ya - yb) * (ya - yb) <= 64 then
        safe = false
        break
    end
end
if safe then
    print('YES')
else
    print('NO')
end
