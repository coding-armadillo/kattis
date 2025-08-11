n, m = io.read("*n", "*n")
r = m - 2 * n
if r % 2 == 1 or r // 2 > n or r < 0 then
    print("Rong talning")
else
    print(r // 2)
end
