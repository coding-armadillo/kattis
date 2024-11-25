a, b, c = [int(d) for d in input().split()]
print(a * b // 2 if a * a + b * b == c * c else -1)
