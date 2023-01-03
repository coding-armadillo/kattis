n = int(input())
s = 0
b = 0
for _ in range(n):
    t = int(input())
    if t > 0:
        b += t
    elif b + t < 0:
        s -= b + t
        b = 0
    else:
        b += t
print(s)
