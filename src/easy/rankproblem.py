n, m = [int(d) for d in input().split()]
ranking = [f"T{i}" for i in range(1, 1 + n)]
for _ in range(m):
    i, j = input().split()
    if ranking.index(i) < ranking.index(j):
        continue
    ranking.remove(j)
    ranking.insert(ranking.index(i) + 1, j)
print(" ".join(ranking))
