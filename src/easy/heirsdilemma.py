l, h = [int(d) for d in input().split()]
total = 0
for i in range(l, h + 1):
    digits = set(str(i))
    if len(digits) != 6 or "0" in digits:
        continue
    if not all([i % int(d) == 0 for d in digits]):
        continue
    total += 1
print(total)
