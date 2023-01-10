for _ in range(int(input())):
    a, b = [int(d) for d in input().split()]
    if a < b or (a + b) % 2:
        print("impossible")
    else:
        print((a + b) // 2, (a - b) // 2)
