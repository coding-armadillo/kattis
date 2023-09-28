import math

tokens = dict([(chr(c), c - ord("A") + 1) for c in range(ord("A"), ord("Z") + 1)])
tokens[" "] = 27
tokens["'"] = 28
t = math.pi * 60 / (28 * 15)
for _ in range(int(input())):
    m = input()
    total = 1
    prev = m[0]
    for c in m[1:]:
        dist = abs(tokens[prev] - tokens[c])
        total += 1 + t * min(dist, 28 - dist)
        prev = c
    print(total)
