n = int(input())
for _ in range(n):
    x = int(input())
    if x % 2:
        res = "odd"
    else:
        res = "even"
    print(f"{x} is {res}")
