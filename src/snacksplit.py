n = int(input())
for _ in range(n):
    g, p = [int(d) for d in input().split()]
    print(g // (p + 1))
