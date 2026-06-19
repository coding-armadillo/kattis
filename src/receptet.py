n = int(input())
v = 0
for _ in range(n):
    h, b, k = [int(d) for d in input().split()]
    if b > h:
        v += (b - h) * k
print(v)
