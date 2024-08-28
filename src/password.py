n = int(input())
p = [float(input().split()[-1]) for _ in range(n)]
print(sum(a * b for a, b in zip(sorted(p, reverse=True), range(1, n + 1))))
