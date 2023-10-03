import math

m = int(input())
t = [int(d) for d in input().split()]
print(f"{math.floor(sum(t)/m)}")
