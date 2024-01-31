n, ta, da, tb, db = io.read("*n", "*n", "*n", "*n", "*n")
a = n * ta + da * (n - 1) * n / 2
b = n * tb + db * (n - 1) * n / 2
if a == b then
    print("=")
elseif a < b then
    print("Alice")
else
    print("Bob")
end
