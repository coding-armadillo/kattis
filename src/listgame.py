import math

x = int(input())

p = 1
total = 0

while x % 2 == 0:
    p = 2
    x /= 2
    total += 1


for i in range(3, math.ceil(math.sqrt(x)) + 1, 2):
    while x % i == 0:
        p = i
        x /= i
        total += 1
if x > 1:
    total += 1


if p == 1:
    total = 1


print(total)
