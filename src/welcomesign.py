r, c = [int(d) for d in input().split()]
t = 0
for i in range(r):
    s = input()
    p = (c - len(s)) // 2
    d = (c - len(s)) % 2
    if t % 2:
        left, right = (p + d) * ".", p * "."
    else:
        right, left = (p + d) * ".", p * "."
    if d:
        t += 1
    print(left + s + right)
