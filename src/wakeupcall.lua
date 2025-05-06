n, m = io.read("*n", "*n")
s1, s2 = 0, 0
for _ = 1, n do
    s1 = s1 + io.read("*n")
end
for _ = 1, m do
    s2 = s2 + io.read("*n")
end
if s1 > s2 then
    print("Button 1")
elseif s1 < s2 then
    print("Button 2")
else
    print("Oh no")
end
