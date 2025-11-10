r, c = [int(d) for d in input().split()]
b = []
for _ in range(r):
    b.append(input())
s = []
for j in range(c):
    col = [b[i][j] for i in range(r)]
    s.append([a for a in col if a != "."].pop())
print(*s, sep="")
