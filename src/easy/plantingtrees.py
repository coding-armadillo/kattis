n = int(input())
t = [int(d) for d in input().split()]

days = [v + d for v, d in zip(sorted(t, reverse=True), range(1, n + 1))]
print(max(days) + 1)
