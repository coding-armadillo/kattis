def p(n):
    if n == 1:
        return 3
    else:
        return p(n - 1) * 2 - 1


n = int(input())
print(p(n) ** 2)
