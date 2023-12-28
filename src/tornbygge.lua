n = io.read("*n")
t = 0
top = 0
for _ = 1, n do
    d = io.read("*n")
    if top == 0 or d > top then
        t = t + 1
    end
    top = d
end
print(t)
