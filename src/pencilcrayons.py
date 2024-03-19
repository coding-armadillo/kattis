n, k = [int(d) for d in input().split()]
t = 0
for _ in range(n):
    t += k - len(set(input().split()))
print(t)
