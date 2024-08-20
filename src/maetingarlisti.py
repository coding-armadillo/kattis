n, r, c = [int(d) for d in input().split()]
a = [input().split() for _ in range(r)]
for i in range(r):
    b = [input() for _ in range(c)]
    if a[i] == b:
        print("left")
    else:
        print("right")
