for _ in range(int(input())):
    _ = input()
    positions = [int(d) for d in input().split()]
    print(2 * (max(positions) - min(positions)))
