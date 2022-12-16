from collections import Counter

hands = [h[0] for h in input().split()]
print(max(Counter(hands).values()))
