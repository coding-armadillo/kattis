n = int(input())
a = sorted([int(d) for d in input().split()], reverse=True)
print(
    sum([a[i] for i in range(0, n, 2)]),
    sum([a[i] for i in range(1, n, 2)]),
)
