n = int(input())
d = 1
while 2 ** (d - 1) < n:
    d += 1
print(d)
