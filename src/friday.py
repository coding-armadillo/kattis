for _ in range(int(input())):
    _, M = [int(d) for d in input().split()]
    d = [int(d) for d in input().split()]
    print(sum(sum(d[:i]) % 7 == 0 and d[i] >= 13 for i in range(M)))
