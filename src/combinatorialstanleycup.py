n = int(input())
if n == 0:
    print(1)
else:
    print(2 ** bin(n).count("1"))
