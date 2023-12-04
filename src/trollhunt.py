b, k, g = [int(d) for d in input().split()]
b -= 1
d = b // (k // g)
if b % (k // g):
    d += 1
print(d)
