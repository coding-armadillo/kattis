a, b, c = [int(d) for d in input().split()]
i, j, k = [int(d) for d in input().split()]
s = min(a / i, b / j, c / k)
print(a - i * s, b - j * s, c - k * s)
