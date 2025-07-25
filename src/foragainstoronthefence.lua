xp, yp = io.read("*n", "*n")
xv, yv = io.read("*n", "*n")
u = io.read("*n")
d = (xp - xv) * (xp - xv) + (yp - yv) * (yp - yv)
if d == u then
    print("on the fence")
elseif d < u then
    print("for")
else
    print("against")
end
