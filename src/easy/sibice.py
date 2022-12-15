import math

n, w, h = [int(d) for d in input().split()]
for _ in range(n):
    line = int(input())
    if line <= math.sqrt(w**2 + h**2):
        print("DA")
    else:
        print("NE")
