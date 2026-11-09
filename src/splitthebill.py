n, m = [int(d) for d in input().split()]
t = sum(int(input()) for _ in range(m))
print(0 if t % n else 1)
