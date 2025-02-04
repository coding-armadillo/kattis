s, p = io.read("*n", "*n")
t = 0
while (true) do
    t = t + s
    m = t * p / 100
    if math.abs(m - s) < 0.0000001 then
        break
    end
    t = t - m
end
print(t)
