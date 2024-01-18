t = int(input())
for _ in range(t):
    n = int(input())
    score = 0
    for _ in range(n):
        x, y = [int(d) for d in input().split()]
        dist = (x**2 + y**2) ** 0.5
        if dist > 200:
            p = 0
        elif dist % 20 == 0:
            p = min(11 - dist // 20, 10)
        else:
            p = 10 - dist // 20
        score += int(p)
    print(score)
