n = int(input())
l = []
for _ in range(n):
    m, o = [int(d) for d in input().split()]
    if not o:
        l.append(m)
print(min(l) if l else -1)
