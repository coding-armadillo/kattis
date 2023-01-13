n = int(input())
b = []
for _ in range(n):
    b.append(input())


def check(b, n):
    for row in b:
        if row.count("W") != row.count("B"):
            return False

        for j in range(0, n - 3):
            if row[j] == row[j + 1] == row[j + 2]:
                return False

    for i in range(n):
        col = ["".join(row[i]) for row in b]

        if col.count("W") != col.count("B"):
            return False

        for j in range(0, n - 3):
            if col[j] == col[j + 1] == col[j + 2]:
                return False

    return True


valid = check(b, n)
print(1 if valid else 0)
