a, b = io.read("*n", "*n")
function gcd(a, b)
	return b == 0 and a or gcd(b, a % b)
end

print(gcd(a, b))
