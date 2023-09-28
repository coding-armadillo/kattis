from collections import Counter

c = Counter(input())
score = 0
for value in c.values():
    score += value**2
if len(c.values()) == 3:
    score += 7 * min(c.values())
print(score)
