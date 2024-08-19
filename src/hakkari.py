n, m = [int(d) for d in input().split()]
res = []
for r in range(n):
    row = input()
    for c in range(m):
        if row[c] == "*":
            res.append((r + 1, c + 1))
print(len(res))
print("\n".join(f"{t[0]} {t[1]}" for t in res))
