from collections import Counter

n, k = [int(d) for d in input().split()]

s = Counter(int(d) for d in input().split())

least = min(s.values())
if len(s.values())< k:
    least=0
ans = 0
c = []
for i in range(k):
    if s[i + 1] == least:
        c.append(str(i + 1))
        ans += 1
print(ans)
print(" ".join(c))
