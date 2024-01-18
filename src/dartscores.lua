t = io.read("*n")
for _ = 1, t do
    n = io.read("*n")
    score = 0
    for _ = 1, n do
        x, y = io.read("*n", "*n")
        dist = (x ^ 2 + y ^ 2) ^ 0.5
        if dist > 200 then
            p = 0
        elseif dist % 20 == 0 then
            p = math.min(11 - dist // 20, 10)
        else
            p = 10 - dist // 20
        end
        score = score + math.floor(p)
    end
    print(score)
end
