def f(n):
    if n < 3:
        return {0: 1, 1: 1, 2: 2}[n]
    else:
        return f(n - 1) + f(n - 2) + f(n - 3)


print(f(int(input())))
