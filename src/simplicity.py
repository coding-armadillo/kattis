from collections import Counter

print(sum([v for _, v in Counter(input()).most_common()[2:]]))
