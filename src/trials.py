from math import sqrt

a, b, c = int(input()), int(input()), int(input())
s = (a + b + c) / 2
print(sqrt(s * (s - a) * (s - b) * (s - c)))
