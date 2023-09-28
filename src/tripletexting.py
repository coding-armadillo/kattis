from collections import Counter

s = input()
times = 3
size = len(s) // times
messages = []
for i in range(0, len(s), size):
    messages.append(s[i : i + size])

original = ""
for i in range(size):
    chars = [m[i] for m in messages]
    if len(set(chars)) == 1:
        original += chars[0]
    else:
        c = Counter(chars)
        original += max(c, key=lambda k: c[k])

print(original)
