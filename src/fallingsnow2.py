n, m = [int(d) for d in input().split()]
g = [input() for _ in range(n)]
s = []
for i in range(m):
    s.append(sum(g[r][i] == "S" for r in range(n)))
for r in range(n):
    print("".join("." if r < n - s[c] else "S" for c in range(m)))
