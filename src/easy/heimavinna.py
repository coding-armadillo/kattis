total = 0
parts = input().split(";")
for part in parts:
    ranges = part.split("-")
    if len(ranges) == 1:
        total += 1
    else:
        total += len(range(int(ranges[0]), int(ranges[1]))) + 1
print(total)
