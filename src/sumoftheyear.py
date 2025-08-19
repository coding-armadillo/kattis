n = int(input())
while True:
    if ((1 + n) * n / 2) ** 2 == sum(i**3 for i in range(1, n + 1)):
        print(n)
        break
    else:
        n -= 1
