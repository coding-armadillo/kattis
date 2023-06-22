n = int(input())
s = input()
a = []
d =""
import string
for i in range(n):
    if s[i] in string.digits:
        d += s[i]

    else:
        if d:
            a.append(int(d))
            d=""
if d :
    a.append(int(d))

print(max(a))
