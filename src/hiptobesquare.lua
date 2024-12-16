for _ = 1, io.read("*n") do
   n = io.read("*n")
   print((math.floor(math.sqrt(n + 1)) - 1) // 2)
end
