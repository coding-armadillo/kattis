m = int(input())
n = int(input())
cars = 0
for _ in range(n):
    cars += input().count(".")
print(cars / (m * n))
