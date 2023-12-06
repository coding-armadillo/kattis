n = int(input())
m = {}
for _ in range(n):
    name, k, t = input().split()
    m[name] = (int(k) + 1) * int(t)

ans = max(m, key=lambda k: m[k])
print(ans, m[ans])
