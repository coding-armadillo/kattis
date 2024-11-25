n, a, b = io.read("*n", "*n", "*n")
fizzbuzz, fizz, buzz = 0, 0, 0
for i = 1, n do
    if i % a == 0 and i % b == 0 then
        fizzbuzz = fizzbuzz + 1
    elseif i % a == 0 then
        fizz = fizz + 1
    elseif i % b == 0 then
        buzz = buzz + 1
    end
end
print(fizz, buzz, fizzbuzz)
