dd, ism, enm, yy = input().split()
m = dict(
    zip(
        "JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC".split(", "),
        range(1, 13),
    )
)
print(f"20{yy}-{m[enm[1:]]:02}-{dd}")
