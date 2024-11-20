a, b = [int(d) for d in input().split()]
va, vb = 0, 0
for _ in range(a):
    c, v = [int(d) for d in input().split()]
    va += c * v
for _ in range(b):
    c, v = [int(d) for d in input().split()]
    vb += c * v
print("same" if va == vb else "different")
