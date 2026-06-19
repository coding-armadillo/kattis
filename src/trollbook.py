n = int(input())
s = []
for _ in range(n):
    a, b = input().split()
    s.append((a, int(b)))
print(" ".join(a for a, _ in sorted(s, key=lambda v: v[1])))
