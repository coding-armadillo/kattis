n = int(input())
m = 0
while n:
    if n % 2:
        n -= 1
        m += 1
    else:
        n //= 2
print(m)
