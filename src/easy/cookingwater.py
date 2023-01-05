n = int(input())
lb, ub = 0, 1000
for _ in range(n):
    a, b = [int(d) for d in input().split()]
    lb = max(lb, a)
    ub = min(ub, b)

if lb > ub:
    print("edward is right")
else:
    print("gunilla has a point")
