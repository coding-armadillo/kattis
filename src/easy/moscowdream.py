a, b, c, n = [int(d) for d in input().split()]

if not all(d > 0 for d in [a, b, c]):
    print("NO")
else:
    print("YES" if a + b + c >= n and n >= 3 else "NO")
