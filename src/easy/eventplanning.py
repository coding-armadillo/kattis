n, b, h, w = [int(d) for d in input().split()]

costs = []
for _ in range(h):
    p = int(input())
    a = [int(d) for d in input().split()]
    if not any([_a >= n for _a in a]):
        costs.append(None)
        continue
    c = p * n
    if c > b:
        c = None
    costs.append(c)

costs = [c for c in costs if c]
if not costs:
    print("stay home")
else:
    print(min(costs))
