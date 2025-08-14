n = int(input())
s = 0
while n != 1:
    if n % 2:
        n += 2 * n + 1
    else:
        n /= 2
    s += 1
print(s)
