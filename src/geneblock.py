mapping = {
    1: 3,
    2: 6,
    3: 9,
    4: 2,
    5: 5,
    6: 8,
    7: 1,
    8: 4,
    9: 7,
    0: 10,
}

for _ in range(int(input())):
    n = int(input())
    d = n % 10

    if n >= 7 * mapping[d]:
        print(mapping[d])
    else:
        print(-1)
