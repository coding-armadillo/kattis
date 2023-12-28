from operator import add, mul, sub, truediv

a, b, c = [int(d) for d in input().split()]
ops = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
}

for op, func in ops.items():
    if a == func(b, c):
        print(f"{a}={b}{op}{c}")
        break
    if func(a, b) == c:
        print(f"{a}{op}{b}={c}")
