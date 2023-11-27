n = int(input())
names = [input() for _ in range(n)]
names = [n for n in names if len(set(n)) == len(n) and len(n) >= 5]
if names:
    least = min(len(n) for n in names)
    names = [n for n in names if len(n) == least]
    print(max(names))
else:
    print("Neibb")
