n = int(input())
total = 0
result = True
for _ in range(n):
    g, b = [int(d) for d in input().split()]
    total += g
    if total < b:
        result = False
print("possible" if result else "impossible")
