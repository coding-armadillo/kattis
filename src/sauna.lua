n = io.read("*n")
ma, mb = -1, 200001
for _ = 1, n do
    a, b = io.read("*n", "*n")
    if a > ma then
        ma = a
    end
    if b < mb then
        mb = b
    end
    if ma > mb then
        break
    end
end
if ma <= mb then
    print(mb - ma + 1, ma)
else
    print('bad news')
end
