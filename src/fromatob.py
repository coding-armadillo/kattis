a, b = [int(d) for d in input().split()]

if a <= b:
    print(b - a)
else:
    total = 0
    while a > b:
        if a % 2:
            a += 1
            total += 1
        a /= 2
        total += 1
    total += b - a
    print(int(total))
