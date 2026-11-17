p, n = [int(d) for d in input().split()]
pj = set(input().split())
ok = []
for i in range(p):
    input()
    s = set(input().split())
    if not s & pj:
        ok.append(i + 1)
print(*ok)
