n, m = [int(d) for d in input().split()]

c = []
for d in range(1, m + 1):
    if d % 3 and d % 5:
        c.append(str(d))
    elif not d % 3 and d % 5:
        c.append("fizz")
    elif d % 3 and not d % 5:
        c.append("buzz")
    else:
        c.append("fizzbuzz")

l = []
for _ in range(n):
    l.append(sum(a == b for a, b in zip(input().split(), c)))
print(l.index(max(l)) + 1)
