a, b = [int(d) for d in input().split()]
c, d = [int(d) for d in input().split()]
t = int(input())
m = abs(a - c) + abs(b - d)
print("Y" if m <= t and (m - t) % 2 == 0 else "N")
