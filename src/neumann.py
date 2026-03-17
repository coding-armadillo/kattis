def f(n):
    if n == 0:
        return "{}"
    else:
        return f'{{{",".join(f(i) for i in range(n))}}}'


print(f(int(input())))
