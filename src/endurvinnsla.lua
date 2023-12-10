_ = io.read()
p, n = io.read("*n", "*n")
total = 0
for _ = 1, n do
    if io.read() == "ekki plast" then
        total = total + 1
    end
end
if total <= p * n then
    print("Jebb")
else
    print("Neibb")
end
