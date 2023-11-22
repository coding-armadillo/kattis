s = io.read()
s, _ = s:gsub("A", "AW")
s, _ = s:gsub("WW", "WAW")
print(s)
