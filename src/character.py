def f(m):
    ans = 0
    for n in range(2, m + 1):
        a, b = 1, 1
        for i in range(m - n + 1, m + 1):
            a *= i
        for i in range(1, n + 1):
            b *= i
        ans += a // b
    return ans


print(f(int(input())))
