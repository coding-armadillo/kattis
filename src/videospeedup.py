n, p, k = [int(d) for d in input().split()]
i = [int(d) for d in input().split()]

start, total = 0, 0
speed = 1
for ti in i:
    total += speed * (ti - start)
    start = ti
    speed += p / 100
total += speed * (k - start)
print(f"{total:.3f}")
