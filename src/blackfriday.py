from collections import Counter

n = input()
a = [int(d) for d in input().split()]
c = Counter(a)
keys = [k for k in c if c[k] == 1]
if not keys:
    print("none")
else:
    print(a.index(max(keys)) + 1)
