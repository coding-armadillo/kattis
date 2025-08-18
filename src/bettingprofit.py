n = int(input())
for _ in range(n):
    m, o, s = input().split()
    m, o = int(m), int(o)
    if s == "+":
        print(m * o / 100)
    elif s == "-":
        print(m * 100 / o)
