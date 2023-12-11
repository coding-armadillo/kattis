n, m = [int(d) for d in input().split()]
cells = []
for _ in range(n):
    cells.append(input())
message = ""
for j in range(m):
    for i in range(n):
        message += cells[i][j] if cells[i][j] != "." else ""
print(message)
