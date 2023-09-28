n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
for d in numbers[::-1]:
    print(d)
