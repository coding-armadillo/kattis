k, m, n = [int(d) for d in input().split()]

print("Barb" if k % (m + n) < m else "Alex")
