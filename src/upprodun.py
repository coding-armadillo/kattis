import math

n, m = int(input()), int(input())

k = math.ceil(m / n)

for _ in range(n - (n * k - m)):
    print("*" * k)
for _ in range(n * k - m):
    print("*" * (k - 1))
