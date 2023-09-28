from collections import Counter

n = int(input())
entries = []
for _ in range(n):
    entries.append(" ".join(sorted(input().split())))

summary = Counter(entries)
popular = max(summary.values())

print(sum([summary[e] for e in summary if summary[e] == popular]))
