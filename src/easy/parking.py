a, b, c = [int(d) for d in input().split()]
t = [0] * 100
for _ in range(3):
    start, end = [int(d) - 1 for d in input().split()]
    for i in range(start, end):
        t[i] += 1

total = 0
mapping = {
    3: c,
    2: b,
    1: a,
}
for s in t:
    total += mapping.get(s, 0) * s
print(total)
