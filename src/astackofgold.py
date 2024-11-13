w, s = [int(d) for d in input().split()]
print((w - s * (s + 1) // 2 * 29260) // 110)
