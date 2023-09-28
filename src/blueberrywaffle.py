r, f = [int(d) for d in input().split()]

a = f // r
b = (f - a * r) / r >= 0.5

print("up" if (a + b) % 2 == 0 else "down")
