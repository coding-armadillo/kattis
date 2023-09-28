n = int(input())
a = [int(d) for d in input().split()] + [0]
print(sum(max(a[i] - a[i + 1] - 1, 0) for i in range(n)))
