import math

a, b = [int(d) for d in input().split("/")]
x, y = 5 * a - 160 * b, 9 * b
gcd = math.gcd(x, y)
x //= gcd
y //= gcd

print(f"{x}/{y}")
