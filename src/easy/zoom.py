n, k = [int(d) for d in input().split()]
x = [int(d) for d in input().split()]
print(" ".join([str(x[i]) for i in range(k - 1, n, k)]))
