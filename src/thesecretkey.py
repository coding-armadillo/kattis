n = int(input())
used = [int(input(), 2) for _ in range(n)]
for i in range(2**n):
    if i not in used:
        valid = i
        break

print(f"{valid:b}".zfill(n))
