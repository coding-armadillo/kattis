n = int(input())
print(n * (n + 1) // 2)
print(sum(i * (i + 1) // 2 for i in range(1, n + 1)))
