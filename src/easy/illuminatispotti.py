n = int(input())
m = []
for _ in range(n):
    m.append(input().split())
total = 0
for i in range(1, n - 1):
    for j in range(i):
        for k in range(i + 1, n):
            if m[i][j] == m[k][j] == m[k][i] == "1":
                total += 1
print(total)
