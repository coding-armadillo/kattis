n, k, d, s = io.read("*n", "*n", "*n", "*n")
ans = (n * d - k * s) / (n - k)
if ans < 0 or ans > 100 then
    print("impossible")
else
    print(ans)
end
