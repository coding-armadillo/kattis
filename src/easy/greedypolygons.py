import math

for _ in range(int(input())):
    n, l, d, g = [int(d) for d in input().split()]
    a = n * l * l / (4 * math.tan(math.pi / n))
    a += n * l * d * g
    a += math.pi * ((d * g) ** 2)
    print(a)
