while True:
    try:
        s = input().split()
    except:
        break

    t1, t2 = s[-2:]

    h1, m1 = [int(d) for d in t1.split(":")]
    h2, m2 = [int(d) for d in t2.split(":")]

    mins = (h2 - h1) * 60 + (m2 - m1)
    h = mins // 60
    m = mins % 60

    ans = s[:-2]
    ans.extend([str(h), "hours", str(m), "minutes"])

    print(" ".join(ans))
