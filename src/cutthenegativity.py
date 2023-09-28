n = int(input())

positives = []
for i in range(n):
    numbers = [int(d) for d in input().split()]
    for j in range(n):
        if numbers[j] > 0:
            positives.append((str(i + 1), str(j + 1), str(numbers[j])))

print(len(positives))
for p in positives:
    print(" ".join(p))
