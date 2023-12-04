n = int(input())
c = [int(d) for d in input().split()]
s = range(1, n + 1)
f = [b / a for a, b in zip(s, sorted(c))]
if max(f) > 1:
    print("impossible")
else:
    print(min(f))
