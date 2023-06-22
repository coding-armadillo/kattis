a, b = [int(d) for d in input().split()]
c = a % b
print(min(c, b - c))
