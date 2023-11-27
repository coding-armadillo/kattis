n, b = [int(d) for d in input().split()]
print("yes" if (2 ** (b + 1)) - 1 >= n else "no")
