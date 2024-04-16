n = int(input())
parts = []
for _ in range(n):
    parts.append(input())
print("".join(p[::-1] for p in parts[::-1]))
