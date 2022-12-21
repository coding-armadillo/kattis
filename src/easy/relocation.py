n, q = [int(d) for d in input().split()]
x = [int(d) for d in input().split()]
for _ in range(q):
    req = [int(d) for d in input().split()]
    if req[0] == 1:
        x[req[1] - 1] = req[2]
    elif req[0] == 2:
        print(abs(x[req[1] - 1] - x[req[2] - 1]))
