from collections import Counter

c = Counter(input())
odds = 0
for v in c.values():
    if v % 2:
        odds += 1
print("no" if odds > 1 else "yes")
