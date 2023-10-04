n, y = [int(d) for d in input().split()]
found = []
for _ in range(y):
    found.append(int(input()))
found = set(found)
for i in range(n):
    if i not in found:
        print(i)
print(f"Mario got {len(found)} of the dangerous obstacles.")
