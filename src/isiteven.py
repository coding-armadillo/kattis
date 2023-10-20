n, k = [int(d) for d in input().split()]

for _ in range(n):
    x = int(input())
    while True:
        if x % 2 == 0:
            x //= 2
            k -= 1
        else:
            break
    if k <= 0:
        break

print(0 if k > 0 else 1)
