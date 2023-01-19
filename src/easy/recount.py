from collections import Counter

c = Counter()
while True:
    try:
        name = input()
    except:
        break
    c[name] += 1

highest = max(c.values())
names = [k for k in c if c[k] == highest]
print("Runoff!" if len(names) > 1 else names.pop())
