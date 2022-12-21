s, t, n = [int(d) for d in input().split()]
ds = [int(d) for d in input().split()]
bs = [int(d) for d in input().split()]
cs = [int(d) for d in input().split()]

for i in range(n):
    s += ds[i]
    if not s % cs[i]:
        wait_b = 0
    else:
        wait_b = cs[i] - s % cs[i]
    s += wait_b + bs[i]

s += ds[n]

if s <= t:
    print("yes")
else:
    print("no")
