n = int(input())
l = []
for _ in range(n):
    m = input().split()[1:]
    l.append([a for a in m if a not in l][0])
print(" ".join(l))
