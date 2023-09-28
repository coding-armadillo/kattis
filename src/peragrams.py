from collections import Counter

s = Counter(input())
v = [d for d in s.values() if d % 2]
v = sorted(v)[:-1]

print(len(v))
