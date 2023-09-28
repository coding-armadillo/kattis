n, k = [int(d) for d in input().split()]
score = 0
for _ in range(k):
    score += int(input())

print((score - 3 * (n - k)) / n, (score + 3 * (n - k)) / n)
