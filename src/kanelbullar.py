a = [int(input()) for _ in range(5)]
b = [int(input()) for _ in range(5)]
print(min(y // x for x, y in zip(a, b)))
