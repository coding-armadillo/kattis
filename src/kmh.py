import math

n = int(input())
m = 0
p = 0
for _ in range(n):
    v = input()
    if v == "/":
        if not m:
            m = 10
        elif m <= p:
            m = 10 * (math.ceil(m / 10) if m % 10 else (m // 10 + 1))
        print(m)
    else:
        v = int(v)
        print(v)
        if v > m:
            m = v
        if v > p:
            p = v
