n, k = [int(d) for d in input().split()]
s = ""
for d in [int(d) for d in input().split()]:
    if d <= k:
        s += "1"
        k -= d
    else:
        s += "0"
print(s)
