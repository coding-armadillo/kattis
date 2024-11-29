n = int(input())
s = input()
wh, wa = 0, 0
rh, ra = 0, 0
for c in s:
    if c == "A":
        ra += 1
    else:
        rh += 1
    if ra == 3 or rh == 3:
        if ra > rh:
            wa += 1
        else:
            wh += 1
        rh, ra = 0, 0
        if wa == n or wh == n:
            break
print("Arnar" if wh > wa else "Hannes")
