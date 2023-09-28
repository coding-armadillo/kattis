def offset(d, b):
    return (b - d % b) % b


cc = 1
while True:
    try:
        a, b = [int(d) for d in input().split()]
    except:
        break

    offset_a, offset_b = offset(a, 365), offset(b, 687)

    if offset_a == offset_b:
        print(f"Case {cc}:", offset_a)
    else:
        t = offset_a
        while True:
            t += 365
            if (offset(t, 687) + offset_b) % 687 == 0:
                break
        print(f"Case {cc}:", t)

    cc += 1
