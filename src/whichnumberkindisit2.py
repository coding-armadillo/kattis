import math

t = int(input())
for _ in range(t):
    n = int(input())
    r = ""
    if n % 2:
        r += "O"
    if math.sqrt(n).is_integer():
        r += "S"
    if not r:
        r = "EMPTY"
    print(r)
