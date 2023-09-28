k = int(input())
a, b = 1, 0
for _ in range(k):
    a, b = b, b + a

print(a, b)
