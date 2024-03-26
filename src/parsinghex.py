import re

h = []
while True:
    try:
        s = input()
        h.extend(re.findall(r"0[xX][0-9a-fA-F]+", s))
    except:
        break
for n in h:
    print(n, int(n, 0))
