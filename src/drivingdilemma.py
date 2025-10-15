s = int(input())
d = float(input())
t = float(input())
print("MADE IT" if d / t <= s * 5280 / 3600 else "FAILED TEST")
