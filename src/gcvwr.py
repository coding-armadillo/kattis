g, t, n = [int(d) for d in input().split()]
capacity = (g - t) * 0.9
items = sum([int(d) for d in input().split()])
print(int(capacity - items))
