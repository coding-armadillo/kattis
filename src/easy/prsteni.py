import math

_ = input()
numbers = [int(d) for d in input().split()]

base = numbers.pop(0)

gcd = [math.gcd(base, n) for n in numbers]

for g, n in zip(gcd, numbers):
    print(f"{int(base/g)}/{int(n/g)}")
