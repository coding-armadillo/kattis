def f(s):
    l, r = range(0, len(s), 2), range(1, len(s), 2)
    lc, rc = "qwertasdfgzxcvb", "yuiophjklnm"
    return (all(s[i] in lc for i in l) and all(s[i] in rc for i in r)) or (
        all(s[i] in lc for i in r) and all(s[i] in rc for i in l)
    )


print("yes" if f(input()) else "no")
