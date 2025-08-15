n = int(input())
d = [int(a) for a in input().split()]
ans = d[0]
for i in range(1, n):
    ans += abs(d[i] - d[i - 1])
print(ans)
