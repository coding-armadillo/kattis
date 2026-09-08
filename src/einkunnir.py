import math

s, n = [int(d) for d in input().split()]
ans = input().split()
for _ in range(n):
    name = input()
    sol = input().split()
    correct = sum(a == b for a, b in zip(ans, sol))
    v = correct / s * 10
    i = math.floor(v)
    f = v - i
    if f < 0.25:
        f = 0
    elif f < 0.75:
        f = 0.5
    else:
        f = 1
    score = i + f

    print(f"{name}: {score:.1f}")
