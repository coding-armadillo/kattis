from collections import Counter

s = input()
d = Counter()

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        d[s[i:j]] += 1

for k in sorted(d, key=lambda k: (-d[k], k)):
    print(d[k], k)
