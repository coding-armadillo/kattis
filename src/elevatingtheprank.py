a, b = [int(d) for d in input().split()]
a, b = min(a, b), max(a, b)
n = int(input())
f = [int(input()) for _ in range(n)]
print((b - a) * 4 + 10 * sum([d > a and d < b for d in f]))
