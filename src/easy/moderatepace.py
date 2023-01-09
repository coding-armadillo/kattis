n = int(input())
distances = [[int(d) for d in input().split()] for _ in range(3)]
plan = [sorted([d[i] for d in distances])[1] for i in range(n)]
print(" ".join([str(d) for d in plan]))
