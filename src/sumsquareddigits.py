for _ in range(int(input())):
    k, b, n = [int(d) for d in input().split()]
    ssd = 0
    while n:
        ssd += (n % b) ** 2
        n //= b
    print(k, ssd)
