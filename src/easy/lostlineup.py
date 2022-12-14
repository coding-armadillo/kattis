n = int(input())
order = [int(d) for d in input().split()]
d = range(1, n)
order = dict(zip(d, order))
ranges = range(1, n + 1)
result = ["1"]
for k in sorted(order, key=lambda x: order[x]):
    result.append(str(ranges[k]))
print(" ".join(result))
