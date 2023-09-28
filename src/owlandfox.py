def sd(n):
    return sum([int(d) for d in str(n)])


for _ in range(int(input())):
    n = int(input())
    s = sd(n) - 1
    d = n - 1
    while True:
        if sd(d) == s:
            break
        d -= 1
    print(d)
