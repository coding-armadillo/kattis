while True:
    n, m = [int(d) for d in input().split()]
    if not n and not m:
        break
    a = [int(input()) for _ in range(n)]
    b = [int(input()) for _ in range(m)]
    total, i, j = 0, 0, 0
    while i < n and j < m:
        if a[i] == b[j]:
            total += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    while i < n:
        if a[i] == b[-1]:
            total += 1
            break
        i += 1
    while j < n:
        if a[-1] == b[j]:
            total += 1
            break
        j += 1
    print(total)
