n = int(input())
c = [int(input()) for d in range(3)]
p = []
for i in range(3):
    if c[i] + n < min([c[j] for j in range(3) if j != i]):
        p.append(c[i] + n)

print("impossible" if not p else min(p))
