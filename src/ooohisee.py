r, c = [int(d) for d in input().split()]
m = []
for _ in range(r):
    m.append(input())

found = []
for i in range(1, r - 1):
    for j in range(1, c - 1):
        if (
            m[i][j] == "0"
            and m[i - 1][j] == "O"
            and m[i][j - 1] == "O"
            and m[i - 1][j - 1] == "O"
            and m[i + 1][j] == "O"
            and m[i][j + 1] == "O"
            and m[i + 1][j + 1] == "O"
            and m[i + 1][j - 1] == "O"
            and m[i - 1][j + 1] == "O"
        ):
            found.append((i + 1, j + 1))

if not found:
    print("Oh no!")
elif len(found) > 1:
    print(f"Oh no! {len(found)} locations")
else:
    print(*found[0])
