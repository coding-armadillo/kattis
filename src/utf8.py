n = int(input())
s = []
for _ in range(n):
    s.append(input())

i = 0
num = 0
err = False
t = [0] * 4
while i < n:
    a = s[i]
    if a.startswith("0") and not num:
        num = 0
        t[0] += 1
    elif a.startswith("110") and not num:
        t[1] += 1
        num = 1
    elif a.startswith("1110") and not num:
        t[2] += 1
        num = 2
    elif a.startswith("11110") and not num:
        t[3] += 1
        num = 3
    elif a.startswith("10") and num:
        num -= 1
    else:
        err = True
        break
    i += 1

if err or num:
    print("invalid")
else:
    print("\n".join([str(d) for d in t]))
