g = [int(d) for d in input().split()]
e = [int(d) for d in input().split()]


def ev(d):
    total, count = 0, 0
    for i in range(d[0], d[1] + 1):
        for j in range(d[2], d[3] + 1):
            total += i + j
            count += 1
    return total / count


ratio = ev(g) / ev(e)
if ratio > 1:
    print("Gunnar")
elif ratio < 1:
    print("Emma")
else:
    print("Tie")
