n = int(input())
a = sorted([int(d) for d in input().split()])
score = sum([(a[j] - a[j + 1]) ** 2 for j in range(n - 1)])
print(score)
