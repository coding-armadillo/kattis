for _ in range(int(input())):
    _ = input()
    n = int(input())
    s = 0
    for _ in range(n):
        s += int(input())
        if s > n:
            s %= n
    print("NO" if s % n else "YES")
