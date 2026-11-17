n = int(input())
for _ in range(n):
    lon, lat = [float(t) for t in input().split()]
    print("INVALID" if any((abs(lon) > 180, abs(lat) > 90)) else "VALID")
