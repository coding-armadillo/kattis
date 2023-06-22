n, m = [int(d) for d in input().split()]
values = [int(d) for d in input().split()]
ans = 0
for i in range(n - m + 1):
    if len([v for v in values[i : i + m] if not v % 2 ]) >= 2:
        ans += 1
print(ans)
