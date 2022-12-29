for _ in range(int(input())):
    k, n = [int(d) for d in input().split()]
    s1 = sum(range(1, n + 1))
    s2 = sum(range(1, 2 * n + 1, 2))
    s3 = sum(range(2, 2 * (n + 1), 2))
    print(k, s1, s2, s3)
