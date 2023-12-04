for _ = 1, io.read("*n") do
    r, e, c = io.read("*n", "*n", "*n")
    if e > r + c then
        print("advertise")
    elseif e < r + c then
        print("do not advertise")
    else
        print("does not matter")
    end
end
