n = int(input())
d = [int(input()) for _ in range(n)]
ans = []
for i in range(2, n + 1):
    if n % i:
        continue
    f = True
    k = n // i
    for j in range(k, n, k):
        if max(d[j - k : j]) >= min(d[j : j + k]):
            f = False
            break
    if f:
        ans.append(str(i))
print("\n".join(ans) if ans else -1)
