for _ in range(int(input())):
    k, n = [int(d) for d in input().split()]
    print(k, int((1 + n) * n / 2 + n))
