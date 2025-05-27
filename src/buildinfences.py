n = int(input())
x, y = [], []
for _ in range(n):
    a, b = [int(d) for d in input().split()]
    x.append(a)
    y.append(b)
print(2 * (max(x) - min(x) + max(y) - min(y) + 4))
