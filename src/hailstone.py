def h(n):
    if n == 1:
        return 1
    else:
        return n + (h(n // 2) if n % 2 == 0 else h(3 * n + 1))


n = int(input())
print(h(n))
