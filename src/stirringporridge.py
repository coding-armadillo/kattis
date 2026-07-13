t = int(input())
l = 0
while True:
    if t - l >= l + 1:
        t -= l
        l += 1
    else:
        break
print(l)
