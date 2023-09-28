h, m = [int(d) for d in input().split()]

mm = m - 45

borrow = 0
if mm < 0:
    mm += 60
    borrow = 1

hh = h - borrow
if hh < 0:
    hh += 24

print(hh, mm)
