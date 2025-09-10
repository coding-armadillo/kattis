n = int(input())
for _ in range(n):
    s = input()[:80]
    print(*[s[i] for i in range(0, len(s), 2)], sep="")
