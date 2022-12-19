n = int(input())
t1, v1 = [float(d) for d in input().split()]
total = 0
for _ in range(n - 1):
    t2, v2 = [float(d) for d in input().split()]
    total += (v1 + v2) * (t2 - t1) / 2
    t1, v1 = t2, v2
total /= 1000
print(total)
