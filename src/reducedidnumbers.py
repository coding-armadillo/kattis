g = int(input())
ids = []
for _ in range(g):
    ids.append(int(input()))

m = 1
while True:
    v = [d % m for d in ids]
    if g == len(set(v)):
        break
    m += 1

print(m)
