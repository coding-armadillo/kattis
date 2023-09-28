import math

n = int(input())
ceil = math.ceil(n / 100) * 100 - 1
floor = math.floor(n / 100) * 100 - 1
if ceil == floor:
    print(ceil)
else:
    if abs(ceil - n) <= abs(n - floor) or floor < 0:
        print(ceil)
    else:
        print(floor)
