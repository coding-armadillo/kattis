a = [int(d) for d in input().split()]
n, kwf = [int(d) for d in input().split()]
s = sum([a[i] * a[i + 1] for i in range(0, 10, 2)])

print(int(int(s / 5) * n / kwf))
