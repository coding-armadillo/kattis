import math

n = int(input())

f = False
for i in range(2, math.ceil(math.sqrt(n)) + 1):
    if n % i == 0:
        f = True
        break
if f:
    print(n - n // i)
else:
    print(n - 1)
