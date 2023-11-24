import math

n = int(input())
m = 2
while True:
    f = True
    for k in range(2, math.ceil(math.sqrt(n * m))):
        if not n * m % (k**2):
            f = False
            break
    if not f:
        m += 1
    else:
        break
print(m)
