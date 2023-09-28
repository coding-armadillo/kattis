cpr = input().replace("-", "")
values = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
total = 0
for d, v in zip(cpr, values):
    total += int(d) * v
if not total % 11:
    print(1)
else:
    print(0)
