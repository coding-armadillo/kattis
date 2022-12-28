r, c = [int(d) for d in input().split()]
parking = []
for _ in range(r):
    parking.append(input())


def count_spaces(parking, squash):
    total = 0
    for i in range(r - 1):
        for j in range(c - 1):
            spaces = [
                parking[i][j],
                parking[i + 1][j],
                parking[i][j + 1],
                parking[i + 1][j + 1],
            ]
            if (
                all(s in ".X" for s in spaces)
                and sum([s == "X" for s in spaces]) == squash
            ):
                total += 1
    return total


for num in range(0, 5):
    print(count_spaces(parking, num))
