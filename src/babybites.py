n = int(input())
a = input().split()
c = [str(d) for d in range(1, n + 1)]
inplace = [i == j if i.isnumeric() and j.isnumeric() else None for i, j in zip(a, c)]
inplace = [v for v in inplace if v is not None]
print("makes sense" if all(inplace) else "something is fishy")
