sh, sm = [int(d) for d in input().split(":")]
eh, em = [int(d) for d in input().split(":")]
dh, dm = 0, 0
dh = eh - sh
if dh < 0:
    dh += 24
dm = em - sm
if dm < 0:
    dm += 60
    dh -= 1
if dh < 0:
    dh += 24
print(60 * dh + dm)
