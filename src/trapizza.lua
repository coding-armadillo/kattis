d, a, b, h = io.read("*n", "*n", "*n", "*n")
m = math.pi * d * d / 4
t = (a + b) * h / 2
if m == t then
    print('Jafn storar!')
elseif m > t then
    print('Mahjong!')
else
    print('Trapizza!')
end
