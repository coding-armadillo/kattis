n = int(input())
for _ in range(n):
    g = [int(d) for d in input().split()][1:]
    prev = g[0]
    for i in range(1, len(g)):
        if g[i] != prev + 1:
            break
        prev = g[i]
    print(i + 1)
