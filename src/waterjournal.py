n, a, b = [int(d) for d in input().split()]
w = [int(input()) for _ in range(n - 1)]
if a in w and b in w:
    print("\n".join([str(d) for d in range(a, b + 1)]))
elif a in w and b not in w:
    print(b)
elif a not in w and b in w:
    print(a)
else:
    print(-1)
