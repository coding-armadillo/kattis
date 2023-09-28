def f(n):
    if n == 0:
        return "{}"
    else:
        ans = ",".join([f(i) for i in range(n)])
        return "{" + ans + "}"


print(f(int(input())))
