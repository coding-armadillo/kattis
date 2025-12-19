from math import sqrt

w, h = [int(d) for d in input().split()]
print(w + h - sqrt(w**2 + h**2))
