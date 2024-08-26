n = int(input())
p = 1
for _ in range(n):
    p *= int(input())
print(p % (10**9 + 7))
