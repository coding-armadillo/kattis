for _ in range(int(input())):
    print(sum([int(d) - 1 for d in input().split()[1:]]) + 1)
