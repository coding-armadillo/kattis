n = int(input())
a, b = 0, 0
f = True
for _ in range(n):
    va, vb = [int(d) for d in input().split()]
    if va < a or vb < b:
        f = False
    else:
        a, b = va, vb
print("yes" if f else "no")
