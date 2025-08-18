m = int(input())
s = []
for _ in range(m):
    s.append([int(d) for d in input().split()][1:])

print(max(max(r) for r in s))
print(min(min(r) for r in s))
print(max(sum(r) for r in s))
print(min(sum(r) for r in s))
