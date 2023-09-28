n, k, today = [int(d) for d in input().split()]
res = 0
for _ in range(n):
    d = int(input())
    if d + 14 - today <= k:
        res += 1
print(res)
