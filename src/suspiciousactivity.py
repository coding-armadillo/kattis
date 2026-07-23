n = int(input())
s = 0
for _ in range(n):
    a, b = [int(d) for d in input().split()]
    if a % 8 and (b < 1 or b > 10000):
        s += 1
print(s)
