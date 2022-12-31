e, f, c = [int(d) for d in input().split()]
total = 0
s = e + f
while s >= c:
    total += s // c
    s = s % c + s // c
print(total)
