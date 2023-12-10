ds, dy, dm, ym = io.read("*n", "*n", "*n", "*n")

for t = 1, 5000 do
    if (t + ds) % dy == 0 and (t + dm) % ym == 0 then
        print(t)
        break
    end
end
