import math

p, q, s = [int(d) for d in input().split()]
print("yes" if p * q / math.gcd(p, q) <= s else "no")
