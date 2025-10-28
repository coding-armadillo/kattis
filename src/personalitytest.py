from collections import Counter

n = int(input())
m = {
    "1": "leader",
    "2": "intellectual",
    "3": "social",
    "4": "practical",
}
for _ in range(n):
    c = Counter(input().split())
    k = max(c, key=c.get)
    print(m[k])
