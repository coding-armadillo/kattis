t = int(input())
for i in range(t):
    _ = input()
    a = sorted([int(d) for d in input().split()])
    b = sorted([int(d) for d in input().split()], reverse=True)
    v = sum(x * y for x, y in zip(a, b))
    print(f"Case #{i+1}: {v}")
