# 22/25


from copy import deepcopy


row, col = [int(d) for d in input().split()]
m = []
for _ in range(row):
    m.append([int(d) for d in input()])

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def reachable(m, r1, c1, r2, c2):
    _m = deepcopy(m)

    q = []
    q.append((r1, c1))
    kind = _m[r1][c1]

    while len(q):
        r, c = q.pop()
        _m[r][c] = -1

        if (r, c) == (r2, c2):
            return True

        for x, y in directions:
            a = r + x
            b = c + y
            if a >= 0 and b >= 0 and a < row and b < col and _m[a][b] == kind:
                q.append((a, b))

    return False


n = int(input())
for _ in range(n):
    r1, c1, r2, c2 = [int(d) - 1 for d in input().split()]
    if reachable(m, r1, c1, r2, c2):
        print("decimal" if m[r1][c1] else "binary")
    else:
        print("neither")
