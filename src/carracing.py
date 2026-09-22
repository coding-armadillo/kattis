n = int(input())
cars = {}
for _ in range(n):
    c, p = [int(d) for d in input().split()]
    if c not in cars:
        cars[c] = [p]
    else:
        cars[c].append(p)
for c in cars:
    cars[c] = int(sum(cars[c]) / len(cars[c]))
best = min(cars, key=lambda v: cars[v])
print(best)
print(cars[best])
