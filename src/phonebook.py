n = int(input())
ans = 0
for _ in range(n):
    s = input()
    if s.startswith("+39") and len(s) in [12, 13]:
        ans += 1
print(ans)
