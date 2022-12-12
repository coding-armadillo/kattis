n = int(input())
for _ in range(n):
    line = input()
    parts = line.split("+")
    if len(parts) == 1:
        print("skipped")
    else:
        print(int(parts[0]) + int(parts[1]))
