n = int(input())
b = None
for _ in range(n):
    d = int(input())
    if not b:
        b = d
        continue

    if d % b == 0:
        print(d)
        b = None
