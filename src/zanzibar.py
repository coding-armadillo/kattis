for _ in range(int(input())):
    numbers = [int(d) for d in input().split()[:-1]]
    total = 0
    for i in range(1, len(numbers)):
        total += max(numbers[i] - 2 * numbers[i - 1], 0)
    print(total)
