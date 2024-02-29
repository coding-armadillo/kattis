n = int(input())
d = [int(d) for d in input().split()]
t = 6 ** (4 - n)
if len(set(d)) < len(d):
    m = 0
else:
    m = 1
    for _ in range(n, 4):
        m *= 6 - n
        n += 1
print(m, t - m)
