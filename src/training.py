n, s = [int(d) for d in input().split()]
for _ in range(n):
    a, b = [int(d) for d in input().split()]
    if s >= a and s <= b:
        s += 1
print(s)
