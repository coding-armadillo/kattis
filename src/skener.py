r, _, zr, zc = [int(d) for d in input().split()]
matrix = []
for _ in range(r):
    matrix.append(input())

ans = []

for row in matrix:
    for i in range(zr):
        ans.append(row)

for row in ans:
    print("".join([col * zc for col in row]))
