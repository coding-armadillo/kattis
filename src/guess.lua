s, e = 1, 1000
while true do
    guess = (s + e) // 2
    print(guess)
    resp = io.read()
    if resp == "correct" then
        break
    elseif resp == "higher" then
        s = guess + 1
    else
        e = guess
    end
end
