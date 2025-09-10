while true do
    a, b = io.read("*n", "*n")
    if a < b then
        print("Less")
    elseif a > b then
        print("More")
    else
        break
    end
end
