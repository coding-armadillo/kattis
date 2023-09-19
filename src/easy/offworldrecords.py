n, c, p = [int(d) for d in input().split()]
ans = 0
for _ in range(n):
    h = int(input())
    if h > c + p:
        ans += 1
        c, p = h, c
print(ans)
