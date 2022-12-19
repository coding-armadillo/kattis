def f(n):
    if n == 1:
        return 1
    else:
        return int(2 * (f(n - 1) + 0.5))


for _ in range(int(input())):
    print(f(int(input())))
