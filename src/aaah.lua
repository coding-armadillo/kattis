a, b = io.read(), io.read()
_, na = a:gsub("a", "")
_, nb = b:gsub("a", "")
if na >= nb then
    print("go")
else
    print("no")
end
