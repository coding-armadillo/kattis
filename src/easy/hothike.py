n = int(input())
t = [int(d) for d in input().split()]
order = sorted(range(n - 2), key=lambda k: max(t[k], t[k + 2]))
d = order[0]
v = max(t[d], t[d + 2])
print(d + 1, v)
