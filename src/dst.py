for _ in range(int(input())):
    f, d, h, m = input().split()
    d, h, m = int(d), int(h), int(m)
    m = m + d if f == "F" else m - d
    h += m // 60
    m = m % 60
    if h >= 24:
        h -= 24
    elif h < 0:
        h += 24
    print(h, m)
