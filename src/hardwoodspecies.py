from collections import Counter

names = []
while True:
    try:
        names.append(input())
    except:
        break
total = len(names)
names = Counter(names)
for n in sorted(names):
    print(n, f"{names[n]/total*100:.6f}")
