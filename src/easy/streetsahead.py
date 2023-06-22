n, q = [int(d) for d in input().split()]

s = {}
for i in range(n):
    s[input()] = i

for _ in range(q):
    a, b = input().split()
    print(abs(s[a] - s[b]) - 1)
