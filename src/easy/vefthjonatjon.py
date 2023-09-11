n = int(input())
parts = [0, 0, 0]
for _ in range(n):
    for i, value in enumerate(input().split()):
        if value == "J":
            parts[i] += 1
print(min(parts))
