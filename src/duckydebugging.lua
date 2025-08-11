while true do
    s = io.read()
    if s == 'I quacked the code!' then
        break
    elseif string.sub(s, -1) == '?' then
        print("Quack!")
    elseif string.sub(s, -1) == '.' then
        print("*Nod*")
    end
end
