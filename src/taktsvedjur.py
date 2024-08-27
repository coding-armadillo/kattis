n = int(input())
m = 1
s = 0
h = 0
while n:
    a = int(input())
    if a > 0:
        h += 1
        if h == 2 * m:
            m = min(m * 2, 8)
            h = 0
    else:
        m = m // 2 or 1
        h = 0

    s += m * a
    n -= 1
print(s)
