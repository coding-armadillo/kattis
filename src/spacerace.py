n = int(input())
_ = input()
d = {}
for _ in range(n):
    entry = input().split()
    d[entry[0]] = float(entry[-1])

print(min(d, key=lambda k: d[k]))
