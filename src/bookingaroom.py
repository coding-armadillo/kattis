r, n = [int(d) for d in input().split()]
booked = [int(input()) for _ in range(n)]
available = set(range(1, 1 + r)) - set(booked)
print("too late" if r == n else available.pop())
