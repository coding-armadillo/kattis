m = int(input())
if m == 2:
    d = 28
elif m in [1, 3, 5, 7, 8, 10, 12]:
    d = 31
else:
    d = 30
print(d)
