xb, yb = [int(d) for d in input().split()]
n = int(input())
safe = True
for _ in range(n):
    xa, ya = [int(d) for d in input().split()]
    if (xa - xb) ** 2 + (ya - yb) ** 2 <= 64:
        safe = False
        break
print("YES" if safe else "NO")
