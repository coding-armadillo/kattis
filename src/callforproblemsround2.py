n, k = [int(d) for d in input().split()]
d = len(set([int(input()) for _ in range(n)]))
print(min(d, k))
