b, d, c, l = [int(d) for d in input().split()]
solved = False
for i in range(l // b + 1):
    for j in range((l - b * i) // d + 1):
        for k in range((l - b * i - d * j) // c + 1):
            if b * i + d * j + c * k == l:
                print(i, j, k)
                solved = True
if not solved:
    print("impossible")
