from collections import Counter

c = Counter()
n = {}

for _ in range(int(input())):
    r = input().split()
    name, course = " ".join(r[:2]), r[-1]
    if course not in n:
        n[course] = set()

    if name not in n[course]:
        c[course] += 1
        n[course].add(name)

for k in sorted(c.keys()):
    print(f"{k} {c[k]}")
