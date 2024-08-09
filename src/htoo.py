import re
from collections import Counter


def f(chemical, k=1):
    res = Counter()
    regex = re.compile(r"(\d+|\w)")
    prev = ""

    for c in regex.split(chemical):
        if c.isalpha():
            res[c] += 1
        elif c.isdigit():
            res[prev] += int(c) - 1
        else:
            continue
        prev = c
    for v in res:
        res[v] *= k
    return res


s, k = input().split()
t = input()

a = f(s, int(k))
b = f(t)

made = True
for v in b:
    if v not in a:
        made = False
        break
    else:
        b[v] = a[v] // b[v]

print(0 if not made else min(b.values()))
