import math

a, _, b = input(), input(), input()
a, b = int(a), int(b)
s = "-" if a / b < 0 else ""
a, b = abs(a), abs(b)
n = math.gcd(a, b)
a //= n
b //= n

if abs(b) == 1:
    print(f"{s}{a}")
else:
    print(f"{s}{a}/{b}")
