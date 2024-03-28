n, k = [int(c) for c in input().split()]
d, s = [int(c) for c in input().split()]
ans = (n * d - k * s) / (n - k)
if ans < 0 or ans > 100:
    print("impossible")
else:
    print(f"{ans:.7f}")
