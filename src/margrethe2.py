from collections import Counter

c = Counter()
n = int(input())
a = []
for _ in range(n):
    p = input()
    f = p.split()[0]
    a.append((p, c[f]))
    c[f] += 1
for p, i in a:
    parts = p.split()
    f = parts[0]
    if c[f] > 1:
        if len(parts) == 1:
            print(f"{p} {i+1}.")
        else:
            print(f, f"{i+1}.", *parts[1:])
    else:
        print(p)
